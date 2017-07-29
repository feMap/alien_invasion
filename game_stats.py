class GameStats():
	"""trace game information"""
	def __init__(self,ai_settings):
		"""initial information"""
		self.ai_settings = ai_settings
		self.reset_stat()

		self.game_active = False

	def reset_stat(self):
		"""initialize the possible change information"""
		self.ships_left = self.ai_settings.ship_limit