import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
	""" alien class """
	def __init__(self,ai_settings,screen):

		super(Alien,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# load image of alien
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# initialize the position of all the aliens
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# save accurate position of aliens
		self.x = float(self.rect.x)

	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def update(self):
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x

	def check_edge(self):
		"""if alien is at the edge of screen,return true"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True





