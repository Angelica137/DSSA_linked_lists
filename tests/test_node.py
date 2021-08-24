from scripts.Node import Node, LinkedList


def test_node_returns_head_value_2():
    head = Node(2)
    assert head.value == 2


def test_node_returns_next_1():
    head = Node(2)
    head.next = Node(1)
    assert head.next.value == 1


'''
def test_node_return_LinkedList():
    linked_list = LinkedList(4)
    linked_list.head.next = Node(3)
    assert linked_list.print_list(linked_list.head.value) == [4, 3]
'''
