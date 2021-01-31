from code_challenges.tree.tree import Node, BinaryTree, BinarySearchTree
import builtins 
import pytest

def test_node_instance():
  groot = Node(4)

  assert groot.value == 4
  assert groot.left == None
  assert groot.right == None

def test_assign_left_right():
  groot = Node('Groot')
  eye = Node('I')
  am = Node('Am')
  groot.left = eye
  groot.right = am
  assert groot.left.value == 'I'
  assert groot.right.value == 'Am'

def test_binary_tree_instance():
  grok = BinaryTree()
  assert grok.root == None
  groot = Node('I am Groot')
  grok.root = groot
  assert grok.root.value == 'I am Groot'
  assert grok.__str__() == 'An instance of a BinaryTree, root is I am Groot'


def test_pre_order():
  grok = BinaryTree()
  groot = Node('Groot')
  i = Node('I')
  am = Node('Am')
  starlord = Node('Future Antman')
  rocket = Node('Trash Panda')
  grok.root = i
  grok.root.left = am
  grok.root.right = starlord
  grok.root.left.left = groot
  grok.root.left.right = rocket
 
  assert grok.pre_order() == ['I','Am', 'Groot', 'Trash Panda', 'Future Antman']


def test_in_order():
  grok = BinaryTree()
  groot = Node('Groot')
  i = Node('I')
  am = Node('Am')
  starlord = Node('Future Antman')
  rocket = Node('Trash Panda')
  grok.root = i
  grok.root.left = am
  grok.root.right = starlord
  grok.root.left.left = groot
  grok.root.left.right = rocket

  assert grok.in_order() == ['Groot', 'Am', 'Trash Panda', 'I', 'Future Antman']


def test_post_order():
  grok = BinaryTree()
  groot = Node('Groot')
  i = Node('I')
  am = Node('Am')
  starlord = Node('Future Antman')
  rocket = Node('Trash Panda')
  grok.root = i
  grok.root.left = am
  grok.root.right = starlord
  grok.root.left.left = groot
  grok.root.left.right = rocket

  assert grok.post_order() == ['Groot', 'Trash Panda', 'Am', 'Future Antman', 'I']