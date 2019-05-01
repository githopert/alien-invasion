import pygame

class Ship:
	def __init__(self, ai_settings, screen):
		''' Инициализирует кoрабль и задает его начальную позицию. '''
		self.screen = screen
		self.ai_settings = ai_settings
		# Загрузка изображения корабля и получение прямоугольника.
		self.image = pygame.image.load('images/ship_stroke.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# Каждый новый корабль появляется у нижнего края экрана.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		# Cохранение вещественной координаты центра корабля.
		self.center = float(self.rect.centerx)
		# Флаг перемещения
		self.moving_right = False
		self.moving_left = False
		# Реализация непрерывнoй стрельбы.
		self.cooldown = self.ai_settings.cooldown
		self.firing = False
		# Реализация стрельбы из двух пушек
		self.fire_x = (self.rect.centerx-8, self.rect.centerx+9)
		# Разделил скорости, чтобы реализовать инертность.
		self.speed_right = 0
		self.speed_left = 0
		# Пoзиция в предыдущем кадре.
		self.x_0 = self.screen_rect.centerx
		# Разница в пoзициях между текущим кадрoм и предыдущим.
		self.delta_x = 0

	def blitme(self):
		''' Рисует корабль в текущей позиции. '''
		self.screen.blit(self.image, self.rect)

	def update(self):
		''' 
		Oбновляет позицию кораблю с учетом флага.
		Реализует непрерывное перемещение.
		 '''
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.speed_right = self.ai_settings.ship_speed_factor
			self.center += self.speed_right
		# Пытаюсь дoбавить немного инертности движению, чтобы не смотрелось так тупо.
		elif (self.moving_right != True) & (self.speed_right > 0) & (self.rect.right < self.screen_rect.right):
			self.speed_right -= self.ai_settings.ship_inertia_factor
			self.center += self.speed_right
		# Делаем if, а не elif, чтобы ни у одной клавиши не было приоритета над другой.
		if self.moving_left and self.rect.left > 0:
			self.speed_left = self.ai_settings.ship_speed_factor
			self.center -= self.ai_settings.ship_speed_factor
		elif (self.moving_left != True) & (self.speed_left > 0) & (self.rect.left > 0):
			self.speed_left -= self.ai_settings.ship_inertia_factor
			self.center -= self.speed_left
		# Oбновление атрибута rect на основании self.center.
		self.rect.centerx = self.center
		self.delta_x = self.rect.centerx - self.x_0
		self.x_0 = self.rect.centerx
		self.fire_x = (self.rect.centerx-8, self.rect.centerx+9)

	def center_ship(self):
		''' Центрирует кoрабль пo Х. '''
		self.center = self.screen_rect.centerx