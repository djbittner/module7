import unittest
from fun_with_collections import sort_and_search_list


class SearchList(unittest.TestCase):
    def test_search_list_found(self):
        self.assertTrue(sort_and_search_list.search_list("yellow"))

    def test_search_list_not_found(self):
        result = sort_and_search_list.search_list("purple")
        self.assertNotEqual(result, -1)


if __name__ == '__main__':
    unittest.main()

