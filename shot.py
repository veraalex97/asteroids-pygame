import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, SHOT_RADIUS)

	def update(self, dt):
		self.position += self.velocity * dt

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius)