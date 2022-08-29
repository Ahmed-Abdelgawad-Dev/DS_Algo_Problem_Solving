

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def search(self, root, key):

        # Base Cases: root is null or key is present at root
        if root is None or root.data == key:
            return root

        # Key is greater than root's key
        if root.data < key:
            return self.search(root.right, key)

        # Key is smaller than root's key
        return self.search(root.left, key)

    # def search(self, parent, data):
    #     if parent is None:
    #         return False
    #     elif parent.data == data:
    #         return True
    #     else:
    #         if data < parent.data:
    #             self.search(parent.left, data)
    #         else:
    #             self.search(parent.right, data)

    def insert(self, parent, data):
        if self.root is None:
            self.root = Node(data)
        else:
            if data < parent.data:
                if parent.left is None:
                    parent.left = Node(data)
                else:
                    self.insert(parent.left, data)
            else:
                if data > parent.data:
                    if parent.right is None:
                        parent.right = Node(data)
                    else:
                        self.insert(parent.right, data)

    def pre_order_traverse(self, subtree):
        if subtree is not None:
            print(subtree.data,  end='       ')
            self.pre_order_traverse(subtree.left)
            self.pre_order_traverse(subtree.right)

    def in_order_traverse(self, subtree):
        if subtree is not None:
            self.in_order_traverse(subtree.left)
            print(subtree.data, end='       ')
            self.in_order_traverse(subtree.right)

    def post_order_traverse(self, subtree):
        if subtree is not None:
            self.post_order_traverse(subtree.left)
            print(subtree.data, end='       ')
            self.post_order_traverse(subtree.right)


tree = BST(Node(10))
tree.root.left = Node(9)
tree.root.right = Node(11)
tree.root.left.left = Node(8)
tree.root.left.right = Node(12)

tree.insert(tree.root, 2)
tree.insert(tree.root, 200)

print('Preorder Traversal: \n \tparent => left => right\n')
tree.pre_order_traverse(tree.root)
print()
print('Ineorder Traversal: \n \tleft => node => right\n')
tree.in_order_traverse(tree.root)
print()
print('Preorder Traversal: \n \tleft => right => parent\n')
tree.post_order_traverse(tree.root)

print()
tree.search(tree.root, 50)
tree.search(tree.root, 200)

