import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.timer = 0


	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return (a, b, c)


	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt


	def move(self, dt):
		forward = pygame.Vector2(0,1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self):
		shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)

		direction = pygame.Vector2(0,1)
		direction = direction.rotate(self.rotation)

		shot.velocity = direction * PLAYER_SHOOT_SPEED


	def update(self, dt):
		self.timer -= dt

		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.rotate(dt * -1)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(dt * -1)
		if keys[pygame.K_SPACE]:
			if self.timer < 0:
				self.shoot()
				self.timer = PLAYER_SHOT_COOLDOWN

