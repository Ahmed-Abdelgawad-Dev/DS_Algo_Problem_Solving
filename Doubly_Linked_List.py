# Doubly Linked List
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        if self.head is None:
            print('the list is empty')
        while self.head:
            print(self.head.data)
            self.head = self.head.next

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None
        self.head.prev = new_node
        self.head = new_node

    def insert_after(self, prev_node, data):
        new_node = Node(data)
        if prev_node is None:
            print('There is no previous node in this linked list')
            return
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next = new_node
        if new_node.next:
            new_node.next.prev = new_node

    def append(self, data):
        new_node = Node(data)
        last = self.head
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last


linked_list = LinkedList()
linked_list.head = Node('Python')
linked_list.push('JavaScript')
linked_list.insert_after(linked_list.head, 'Django')
linked_list.append('React')
linked_list.print_list()
