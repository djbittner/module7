"""
Author:  Derek Bittner
Due Date:  10/13/2020
Program:  sort_and_search_array.py

"""

import array as arr

myFruit = ["Apples", "bananas", "cherries", "grapes"]


def search_array(c):
    if c in myFruit:
        return myFruit.index(c)
    else:
        return "-1"


def sort_array():
    myFruit.sort()
    sorted_arr = arr.array
    return myFruit


if __name__ == '__main__':
    search_array("bananas")
    sort_array()
