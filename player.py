import random
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
    
    def rocket(self):
        # Forward direction based on the player's rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Forward vector
        right = pygame.Vector2(1, 0).rotate(self.rotation) * self.radius / 2  # Right vector for width

        # Rocket body vertices
        nose = self.position + forward * self.radius  # Nose of the rocket
        left_fin = self.position - forward * self.radius + right * 1.5  # Left fin base
        right_fin = self.position - forward * self.radius - right * 1.5  # Right fin base
        tail_left = self.position + right  # Tail left corner
        tail_right = self.position - right  # Tail right corner

        # Return the vertices as a polygon
        return [nose, left_fin, tail_left, tail_right, right_fin]
    
    def rocket_fire(self):
        # Calculate bottom center of the rocket where fire will emit
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Forward vector
        right = pygame.Vector2(1, 0).rotate(self.rotation) * self.radius / 3  # Right vector for width
        tail_center = self.position - forward * (self.radius + 5)  # Fire below the tail

        # Fire flicker effect with random variation
        fire_tip = tail_center - forward * random.randint(10, 20)
        left_fire = tail_center + right
        right_fire = tail_center - right

        return [fire_tip, left_fire, right_fire]
    
    def draw(self, screen):
        #Draw the rocket
        pygame.draw.polygon(screen, "white", self.rocket(), 2)
        # Draw the rocket fire
        pygame.draw.polygon(screen, "orange", self.rocket_fire())
        return super().draw(screen)
    

    
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        
        #Shooting Cooldown timer
        self.shoot_timer -= dt

        #Player's inertia and drag
        self.velocity *= PLAYER_FRICTION
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
        
        