from collections import OrderedDict

class Enterprise:
    """Common base class for all enterprises"""

    def __init__(self, name, valid_num, invalid_num, survey):
        self.enterprise_name = name
        self.valid_num = valid_num
        self.invalid_num = invalid_num
        self.survey = survey

    def display_summary(self):
        print(self.enterprise_name)
        d_descending = OrderedDict(sorted(self.survey.items(), 
            key=lambda k: k[1]['fav'], reverse=True))
        for k, v in d_descending.items():
            sum = v['fav'] + v['neutral'] + v['unfav']
            print('{}: {}% fav, {}% neutral, {}% unfav'
                .format(k, int(v['fav']/sum*100), 
                    int(v['neutral']/sum*100), 
                    int(v['unfav']/sum*100)))
        print('\n')
    def get_ids_from_survey(self):
        id_list = []
        for k in self.survey.items():
            id_list.append(k[0])
        return id_list

    def get_valid_answer(self):
        return self.enterprise_name, self.valid_num

    def get_invalid_answer(self):
        return self.enterprise_name, self.invalid_num

    def get_fav_answer_by_id(self, id):
        sum = self.survey[id]['fav'] + self.survey[id]['neutral'] +\
        self.survey[id]['unfav']
        return(self.enterprise_name,
            int(self.survey[id]['fav']/sum*100))