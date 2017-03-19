from collections import OrderedDict

class Enterprise:
    """Common base class for all enterprises"""
    countEnterprise = 0
    def __init__(self, name, valid_num, invalid_num, survey):
        self.enterprise_name = name
        self.valid_num = valid_num
        self.invalid_num = invalid_num
        self.survey = survey
        Enterprise.countEnterprise += 1

    def sort_survey():
        return OrderedDict(sorted(survey.items()))

    def displayVariables(self):
        print ( "{}\n" 
                "Favoral checks:    {}\n" 
                "Unfavoral checks:  {}\n" 
                "Neutral checks:    {}\n" 
                "Invalid checks:    {}\n"
                .format(self.enterprise_name, self.fav_num, self.unfav_num,
                        self.neutral_num, self.invalid_num))

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