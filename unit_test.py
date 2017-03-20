import unittest
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


if __name__ == '__main__':
    unittest.main()
