from scripts.Exercise3 import create_linkedList


def test_create_linkedList_returns_head():
    assert create_linkedList([1, 2, 3]) == 1
