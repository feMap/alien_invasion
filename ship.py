import pygame


class Ship():
	def __init__(self,ai_settings,screen):
		"""initialize"""
		self.screen = screen
		self.ai_settings = ai_settings

		# load ship image and rec
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# new ship show in the mid bottom
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# ship center save velocity
		self.center = float(self.rect.centerx)


		# moving stat parameter
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""move ship according the mark"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			# self.rect.centerx += 1
			self.center += self.ai_settings.ship_speed_factor

		if self.moving_left and self.rect.left > 0:
			# self.rect.centerx -= 1
			self.center -= self.ai_settings.ship_speed_factor

		# change the rect instance according to te self.center
		self.rect.centerx = self.center



	def blitme(self):
		"""paint ship in right position"""
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		"""let the ship in the middle of screen"""
		self.center = self.screen_rect.centerx