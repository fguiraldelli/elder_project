from collections import OrderedDict

class Enterprise:
    """Common base class for all enterprises"""
    countEnterprise = 0
    def __init__(self, name, valid_num, invalid_num, survey):
        self.enterprise_name = name
        self.valid_num = valid_num
        self.invalid_num = invalid_num
        self.survey = survey
        #self.survey = OrderedDict(sorted(survey.items()))
        Enterprise.countEnterprise += 1

    def display_summary(self):
        print(self.enterprise_name)
        d_descending = OrderedDict(sorted(self.survey.items(), 
            key=lambda k: k[1]['fav'], reverse=True))
        for k, v in d_descending.items():
            sum = v['fav'] + v['neutral'] + v['unfav']
            print('{}: {:.0%} fav, {:.0%} neutral, {:.0%} unfav'
                .format(k, v['fav']/sum, v['neutral']/sum, 
                    v['unfav']/sum))
        print('\n')

    def get_valid_answer(self):
        return self.enterprise_name, self.valid_num

    def get_invalid_answer(self):
        return self.enterprise_name, self.invalid_num

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