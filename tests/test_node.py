from scripts.node import Node


def test_node_returns_head_value_2():
    head = Node(2, 1)
    assert head.value == 2
