class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = Node(head)

    def print_list(self, head):
        current_node = self.head
        while current_node != None:
            print(current_node.value)
            current_node = current_node.next


'''
linked_list = LinkedList(4)
linked_list.head.next = Node(3)
linked_list.print_list(linked_list.head.value)
'''
