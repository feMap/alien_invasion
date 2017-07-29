# coding: utf-8

class Settings():
	"""save all Alient_Invasion class"""

	def __init__(self):
		""" initialize"""
		# screen setting
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)

		# ship setting
		self.ship_limit = 3

		# self.ship_speed_factor = 1.5

		# bullet setting
		# self.bullet_speed_factor = 1
		# self.bullet_width = 3
		self.bullet_width = 900
		self.bullet_height = 15
		self.bullet_color = 60,60,60

		self.bullets_allowed = 5

		# aliens setting
		# self.alien_speed_factor = 0.7
		self.fleet_drop_speed = 50

		self.speedup_scale = 1.1
		self.initialize_dynamic_settings()


		# -1 is right, 1 is left
		self.fleet_direction = 1

	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 0.6

		# fleet direction setting
		self.fleet_direction = 1.1

	def increase_speed(self):
		# 增加速度
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale