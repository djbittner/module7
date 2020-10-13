"""
Author:  Derek Bittner
Due Date:  10/13/2020
Program:  sort_and_search_list.py

"""


myList = ["red", "orange", "yellow", "green", "blue"]


def search_list(c):
    if c in myList:
        return myList.index(c)
    else:
        return "-1"


def sort_list():
    myList.sort()
    sorted_list = myList
    return myList


if __name__ == '__main__':
    search_list("yellow")
    sort_list()

