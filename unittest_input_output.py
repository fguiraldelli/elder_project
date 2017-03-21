import unittest
import input_output

class TestInputOutputMethods(unittest.TestCase):

    def test_create_file_list(self):
        input_list = []
        for i in range(3):
            input_list.append('input'+str(i))
        input_list.remove(input_list[0])
        list_of_enterprises, list_of_files = input_output.create_file_list(input_list)
        self.assertEqual(list_of_files, input_list)
        self.assertEqual(list_of_enterprises, [])

    def test_init_question(self):
        #Testing favorable answer
        dict_res = input_output.init_question(0)
        self.assertGreater(dict_res['fav'], 0)
        dict_res = input_output.init_question(1)
        self.assertGreater(dict_res['fav'], 0)
        #Testing neutral answer
        dict_res = input_output.init_question(2)
        self.assertGreater(dict_res['neutral'], 0)
        #Testing unfavorable answer
        dict_res = input_output.init_question(3)
        self.assertGreater(dict_res['unfav'], 0)
        dict_res = input_output.init_question(4)
        self.assertGreater(dict_res['unfav'], 0)

    def test_count_answer_type(self):
        dict_type_question ={'fav':0, 'neutral':0, 'unfav':0}
        #Testing favorable answer
        dict_res = input_output.count_answer_type(dict_type_question, 1)
        dict_res = input_output.count_answer_type(dict_res, 0)
        self.assertGreater(dict_res['fav'], 1)
        #Testing neutral answer
        dict_res = input_output.count_answer_type(dict_res, 2)
        dict_res = input_output.count_answer_type(dict_res, 2)
        self.assertGreater(dict_res['neutral'], 1)
        #Testing unfavorable answer
        dict_res = input_output.count_answer_type(dict_res, 3)
        dict_res = input_output.count_answer_type(dict_res, 4)
        self.assertGreater(dict_res['unfav'], 1)

if __name__ == '__main__':
    unittest.main()
