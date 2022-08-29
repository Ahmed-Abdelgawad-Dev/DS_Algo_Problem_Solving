class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = None
        self.tail = None

    def show_list(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        new_node.next = self.head
        self.head = new_node
    
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print('This node is not in the list')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, node, value):
        while node.data is not value:
            node = node.next
        node.data = node.next.data
        node.next = node.next.next
    def delete_node_after(self, node):
        if node and node.next:
            node_to_del = node.next         # deleted node = node position + 1 
            # node.data = node_to_del.data    # set curr node data to equal the deleted node
            node.next = node_to_del.next    # assign node pointer to the same position of deleted node pointer
    def delete_node_again(self, node):
        node.data = node.next.data
        node.next = node.next.next

linked_list = LinkedList()
linked_list.head = Node(1)
linked_list.append(9)
linked_list.append(10)
linked_list.append(11)
linked_list.prepend(100)
linked_list.insert_after_node(linked_list.head.next, 1000)
linked_list.delete_node(linked_list.head, 100)
linked_list.delete_node_after(linked_list.head)
linked_list.delete_node_again(linked_list.head.next.next)
linked_list.show_list()
