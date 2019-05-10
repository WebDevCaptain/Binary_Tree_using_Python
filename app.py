from node import Node
from binary_tree import BinaryTree

tree = BinaryTree(Node(20))

my_nums = [2, 44, 5, 33, 90, 76, 16]
for i in my_nums:
    tree.add(Node(i))

tree.inorder()
tree.delete(90)
tree.delete(44)
tree.inorder()
