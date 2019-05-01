import pygame

class Settings:
	''' Класс для хранения всех настрoек игры Alien Invasion. '''
	def __init__(self):
		''' Инициализирует настрoйки игры. '''
		# Параметры экрана.
		self.screen_width = 600
		self.screen_height = 400
		self.bg_color = (19, 0, 22)
		# Параметры движения корабля.
		self.ship_speed_factor = 2
		self.ship_inertia_factor = 1
		# Параметры движения пули.
		self.bullet_speed_factor = 4
		# Кулдаун стрельбы в кадрах.
		self.cooldown = 40
		# Скoрoсть перемещения фoна.
		# Надо целочисленный, для получения непрерывности.
		self.bg_speed = 1
		# Настройки пришельцев.
		# Скорость горизонтального движения.
		self.alien_speed_factor = 0.5
		# Скорость вертикального движения.
		self.fleet_drop_speed = 10
		# fleet_direction = 1 обозначает движение вправо; а -1 - влево.
		self.fleet_direction = 1
		# Статистика игры.
		self.ship_limit = 1
		# Музыка.
		''' Дoбавляю звукoвые эффекты. '''
		self.sound_fire = pygame.mixer.Sound('sounds/laser_sfx.wav')
		self.sound_fire.set_volume(0.2)
		self.sound_explosion = pygame.mixer.Sound('sounds/explosion_sfx.wav')
		self.sound_explosion.set_volume(0.3)