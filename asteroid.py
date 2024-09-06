import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        return super().draw(screen)
    
    def update(self, dt):
        self.position += self.velocity * dt 
        return super().update(dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            velocity1 = pygame.Vector2.rotate(self.velocity,random_angle)
            velocity2 = pygame.Vector2.rotate(self.velocity,-1 * random_angle)
            splitted_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, splitted_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, splitted_radius)
            asteroid1.velocity = velocity1 * 1.2
            asteroid2.velocity = velocity2 * 1.2