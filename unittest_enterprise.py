import unittest
import enterprise

class TestEnterpriseClass(unittest.TestCase):

    def setUp(self):
        survey = {4568: {'fav': 2, 'neutral': 0, 'unfav': 1}, 4569: 
        {'fav': 0, 'neutral': 1, 'unfav': 0}, 4570: {'fav': 1, 'neutral': 0,
         'unfav': 1}, 4571: {'fav': 1, 'neutral': 0, 'unfav': 1}, 4567: 
         {'fav': 0, 'neutral': 1, 'unfav': 0}}

        self.company = enterprise.Enterprise('TestCompany', 9, 1, survey)

    def test_get_valid_answer(self):
        valid_answer = self.company.get_valid_answer()
        self.assertEqual(valid_answer[1], 9)

    def test_get_invalid_answer(self):
        invalid_answer = self.company.get_invalid_answer()
        self.assertEqual(invalid_answer[1], 1)

    def test_get_ids_from_survey(self):
        list_expected = [4568, 4569, 4570, 4571, 4567]
        ids = self.company.get_ids_from_survey()
        self.assertListEqual(ids, list_expected)

    def test_get_fav_answer_by_id(self):
        list_expected = [('TestCompany', 66), ('TestCompany', 0), 
        ('TestCompany', 50), ('TestCompany', 50), ('TestCompany', 0)]
        ids_list = [4568, 4569, 4570, 4571, 4567]
        result_list = []
        for i in ids_list:
            result_list.append(self.company.get_fav_answer_by_id(i))
        self.assertListEqual(result_list, list_expected)


if __name__ == '__main__':
    unittest.main()
