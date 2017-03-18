class Question:
	"""docstring for ClassName"""
	def __init__(self):
		self.question_number = 0
		self.favoral = 0
		self.neutral = 0
		self.unfavoral = 0

	def displayQuestionStatistics(self):
		if self.question_number == 0:
			print('{}: {}% fav, {}% neutral, {}% unfav'
				.format(self.question_number, self.favoral,
				 self.neutral, self.unfavoral))