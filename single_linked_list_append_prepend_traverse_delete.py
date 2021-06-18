class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self, head=None):
		self.head = head

	# O(n) as each node is accessed, O(1) if not.
	def traverse(self):
		current_node = self.head
		while current_node:
			print(current_node.data)
			current_node = current_node.next

	# Adding node in the beginning
	def prepend(self, item):
		new_node = Node(item)
		if not self.head:
			new_node.next = self.head
			self.head = new_node

	# Adding node at the end
	def append(self, item):
		new_node = Node(item)
		if self.head is None:
			self.head = new_node
			return
		last = self.head
		while last.next:
			last = last.next
		last.next = new_node

	# Adding node in a specific place
	def inject_node(self, prev_node, new_data):
		new_node = Node(new_data)
		if prev_node is None:
			print('the node is not in the linked list')
		new_node.next = prev_node.next
		prev_node.next = new_node

	def del_node(self, node):
		if node is None:
			return
		node.data, node.next = node.next.data, node.next.next


if __name__ == '__main__':
	my_list = LinkedList()
	my_list.head = Node('one')
	my_list.head.next = Node('Two')
	my_list.head.next.next = Node('Three')
	my_list.prepend('New Head')
	my_list.append('Last')
	my_list.inject_node(my_list.head.next.next, 'Injected Node')
	print('-------------Before Deleting a node-----------------:')
	my_list.traverse()
	my_list.del_node(my_list.head.next)
	print('-------------After deleting a node-----------------:')
	my_list.traverse()
