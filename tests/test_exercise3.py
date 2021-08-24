from scripts.Exercise3 import create_linked_list
#from scripts.Node import Node


def test_create_linkedList_returns_head():
    assert create_linked_list([1, 2, 3]) == 1
