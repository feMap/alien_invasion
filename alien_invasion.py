# coding: utf-8

import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

from pygame.sprite import Group

from alien import Alien

from game_stats import GameStats

from button import Button

def run_game():
	# initialize
	pygame.init()

	ai_settings = Settings()

	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

	pygame.display.set_caption("Alien Invasion")

	# 创建play按钮
	play_button = Button(ai_settings,screen,"Play")

	# create a instance to storage the GameStats
	stats = GameStats(ai_settings)

	# # set backgroud color
	# bg_color = (230,230,230)

	ship = Ship(ai_settings,screen)

	# create a group to save the bullet
	bullets = Group()

	# create aliens
	# alien = Alien(ai_settings,screen)

	aliens = Group()

	gf.create_fleet(ai_settings,screen,ship,aliens)

	# begin loop
	while True:

		# # every loop repaint bgColor
		# screen.fill(ai_settings.bg_color)

		# # paint ship
		# ship.blitme()

		# # keyboard and mouse
		# for event in pygame.event.get():
		# 	if event.type == pygame.QUIT:
		# 		sys.exit()

		gf.check_e vents(ai_settings,screen,stats,play_button,ship,aliens,bullets)

		if stats.game_active:
			
			ship.update()

			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
 
			gf.update_bullets(ai_settings,screen,ship,aliens,bullets)

		# # display
		# pygame.display.flip()

		gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button)

		# print(len(bullets)) 


run_game()