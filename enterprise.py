class Enterprise:
	'Common base class for all enterprises'
	countEnterprise = 0
	valid_num = 0
	def __init__(self, enterprise_name, fav_num, neutral_num, unfav_num,
	 invalid_num):
		self.enterprise_name = enterprise_name
		self.fav_num = fav_num
		self.neutral_num = neutral_num
		self.unfav_num = unfav_num
		self.invalid_num = invalid_num
		Enterprise.countEnterprise += 1

	def displayVariables(self):
		print (	"Enterprise name: 	{}\n" 
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

emp1 = Enterprise('XPTO', 500, 150, 100, 250)
emp1.displayVariables()
emp1.displayValidNumbers()
emp1.displayInvalidNumbers()
