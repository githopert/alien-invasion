class GameStats():
	''' Oтслеживание внутриигровой статистики Alien Invasion. '''
	def __init__(self, ai_settings):
		''' Инициализирует внутриигровую статистику. '''
		self.ai_settings = ai_settings
		self.game_active = False
		# В начале игры создается вся статистика.
		# Вызов метода внутри класса!
		self.reset_stats()

	def reset_stats(self):
		''' Инициализирует статистику, изменяющуюся в ходе игры. '''
		self.ships_left = self.ai_settings.ship_limit
