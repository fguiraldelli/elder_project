from collections import OrderedDict

class Enterprise:
    """Common base class for all enterprises"""
    countEnterprise = 0
    def __init__(self, name, valid_num, invalid_num, survey):
        self.enterprise_name = name
        self.valid_num = valid_num
        self.invalid_num = invalid_num
        self.survey = OrderedDict(sorted(survey.items()))
        Enterprise.countEnterprise += 1

    def calculate_percentage(self):
        for k, v in self.survey.items():
            print(v)

    def displayValidNumbers(self):
        print ("The valid pool's number is: {}\n".format(self.fav_num
            +self.neutral_num+self.unfav_num))

    def displayInvalidNumbers(self):
        print ("Total of invalid numbers: {}\n".format(self.invalid_num))

    def displayStatistics(self):
        print(
            "Enterprise name:   {}\n"
            "Valid answers:     {}\n"
            "Invalid answers:   {}\n"
            "Survey:            {}\n"
            .format(self.enterprise_name,
                self.valid_num,
                self.invalid_num,
                self.survey)
            )