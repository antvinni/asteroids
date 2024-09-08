import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shoot_timer = 0
        self.num_lifes = PLAYER_NUM_LIFES
        self.score = 0
        self.forward = True 

    #make a player look like triangle (though hitbox remains to be a circle)
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        return super().draw(screen)
    
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        
        #Shooting Cooldown timer
        self.shoot_timer -= dt

        #Player's inertia and drag
        self.velocity *= 0.98
        if self.forward == True:
            self.position += self.velocity * dt
        else:
            self.position += self.velocity * -dt
        #Player Actions
        
        keys = pygame.key.get_pressed()
        

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
            self.forward = True
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
            self.forward = False
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        self.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_START_SPEED
        self.position += self.velocity * dt
        

    def shoot(self):
        if self.shoot_timer > 0:
            pass
        else:
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        
        