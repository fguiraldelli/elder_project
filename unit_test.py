import unittest
import enterprise
import rank

class TestRankMethods(unittest.TestCase):

    def test_create_file_list(self):
        input_list = []
        for i in range(3):
            input_list.append('input'+str(i))
        input_list.remove(input_list[0])
        list_of_enterprises, list_of_files = rank.create_file_list(input_list)
        self.assertEqual(list_of_files, input_list)
        self.assertEqual(list_of_enterprises, [])

    def test_count_answer_type(self):
        dict_type_question ={'fav':0, 'neutral':0, 'unfav':0}
        dict_res_fav ={'fav':1, 'neutral':0, 'unfav':0}
        dic_res={}
        # dict_res_neutral ={'fav':0, 'neutral':1, 'unfav':0}
        # dict_res_unfav = {'fav':0, 'neutral':0, 'unfav':1}

        #Testing favoral answer
        dict_res = rank.count_answer_type(dict_type_question, 1)
        #self.assertDictEqual(dict_res, dict_res_fav)
        self.assertGreater(dict_res['fav'], 0)

if __name__ == '__main__':
    unittest.main()
