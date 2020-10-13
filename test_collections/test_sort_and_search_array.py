import unittest
from fun_with_collections import sort_and_search_array


class SearchList(unittest.TestCase):
    def test_search_array_found(self):
        self.assertTrue(sort_and_search_array.search_array("bananas"))

    def test_search_array_not_found(self):
        result = sort_and_search_array.search_array("oranges")
        self.assertNotEqual(result, -1)



if __name__ == '__main__':
    unittest.main()
