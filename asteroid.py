import pygame as p
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import random

class Asteroid(CircleShape):
    containers = None
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, screen):
        p.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        new_velocity = self.velocity.rotate(angle)
        new_velocity_negative = self.velocity.rotate(angle * - 1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius) # type: ignore
        a2 = Asteroid(self.position.x, self.position.y, new_radius) # type: ignore 
        a1.velocity = new_velocity * 1.2
        a2.velocity = new_velocity_negative * 1.2
        
