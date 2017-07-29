# coding: utf-8

import sys

import pygame

from bullet import Bullet

from alien import Alien

from time import sleep

def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets):
	"""mouse and keyboard action"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
	
	button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		# 重置游戏设置
		ai_settings.initialize_dynamic_settings()

		# 重置游戏统计信息
		stats.reset_stat()
		stats.game_active = True

		# 隐藏光标
		pygame.mouse.set_visible(False)

		# 清空外信任列表和子弹列表
		aliens.empty()
		bullets.empty()

		# 创建一群新的外星人,并让飞机居中
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)

	elif event.key == pygame.K_q:
		sys.exit()
		

def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False

def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		# create a bullet, and add it to a group
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)

def update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button):
	screen.fill(ai_settings.bg_color)

	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	# alien.blitme()
	aliens.draw(screen)

	# if game is not active, then draw the play_button
	if not stats.game_active:
		play_button.draw_button()

	# display the screen
	pygame.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets):
	"""update bullet position"""
	bullets.update()

	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)
	

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
	"""Action do with interaction between aliens and bullets"""
	# check whether hit the alien
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

	if len(aliens) == 0:
		# delete all bullets and create a new group of aliens
		bullets.empty()
		ai_settings.increase_speed()
		create_fleet(ai_settings,screen,ship,aliens)

def create_fleet(ai_settings,screen,ship,aliens):
	""" create a group of aliens """

	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width

	number_aliens_x = get_number_aliens_x(ai_settings,alien_width)
	row_number = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

	# create first line of alien
	for row_number in range(row_number):
		for alien_number in range(number_aliens_x):
			# # create first alien
			# alien = Alien(ai_settings,screen)
			# alien.x = alien_width + 2 * alien_width * alien_number
			# alien.rect.x = alien.x
			# aliens.add(alien)
			create_alien(ai_settings,screen,aliens,alien_number,row_number)

def get_number_aliens_x(ai_settings,alien_width):
	"""calculate the number of aliens each line"""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x/(2 * alien_width))
	return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
	"""calculate the available rows in screen """
	available_space_y = (ai_settings.screen_height-3 * alien_height - ship_height)

	number_rows = int(available_space_y/(2*alien_height))

	return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):

	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
 
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

	aliens.add(alien)

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
	"""update all aliens position of aliens"""

	check_fleet_edge(ai_settings,aliens)

	aliens.update()

	# check whether the interactions between aliens and ship
	if pygame.sprite.spritecollideany(ship,aliens):
		# print 'Ship hit!!!'
		ship_hit(ai_settings,stats,screen,ship,aliens,bullets)

	check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)

def check_fleet_edge(ai_settings,aliens):
	"""when aliens rearch the edge and do something"""
	for alien in aliens.sprites():
		if alien.check_edge():
			change_fleet_direction(ai_settings,aliens)
			break

def change_fleet_direction(ai_settings,aliens):
	"""moving down the aliens, and change their direction"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed

	ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
	"""reaction of the ship"""
	if stats.ships_left > 0:
		# ship_left - 1
		stats.ships_left -= 1

		# clear alien group and bullet group
		aliens.empty()
		bullets.empty()

		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()

		# pause
		sleep(2)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
	""" check whether aliens reach the bottom of screen"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# act like the crash of ship
			ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
			break

