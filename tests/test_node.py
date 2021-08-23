from scripts.Node import Node


def test_node_returns_head_value_2():
    head = Node(2)
    assert head.value == 2


def test_node_returns_next_1():
    head = Node(2)
    head.next = Node(1)
    assert head.next.value == 1
