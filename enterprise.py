class Enterprise:
	'Common base class for all enterprises'

	list_of_questions = []
	enterprise_name = ""
	countEnterprise = 0
	valid_num = 0
	fav_num = 0
	neutral_num = 0
	unfav_num = 0
	invalid_num = 0

	def __init__(self):
		Enterprise.countEnterprise += 1

	def displayVariables(self):
		print (	"{}\n" 
				"Favoral checks: 	{}\n" 
				"Unfavoral checks: 	{}\n" 
				"Neutral checks: 	{}\n" 
				"Invalid checks: 	{}\n"
				.format(self.enterprise_name, self.fav_num, self.unfav_num,
						self.neutral_num, self.invalid_num))

	def displayValidNumbers(self):
		print ("The valid pool's number is: {}\n".format(self.fav_num
			+self.neutral_num+self.unfav_num))

	def displayInvalidNumbers(self):
		print ("Total of invalid numbers: {}\n".format(self.invalid_num))
