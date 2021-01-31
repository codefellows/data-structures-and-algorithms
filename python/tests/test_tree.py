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
  assert grok.__repr__() == 'An instance of a BinaryTree, root is I am Groot'


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

def test_bst_instance():
  hal = BinarySearchTree()
  assert hal.root == None
  hal.root = Node(9)
  assert hal.root.value == 9

def test_bst_contains_false():
  hal = BinarySearchTree()
  jarvis = Node(9)
  mr_robot = Node(3) 
  dva = Node(4) 
  navi = Node(5) 
  gdi = Node(7) 
  nod = Node(2) 
  ghost = Node(6) 
  winter = Node(1) 
  navi.left = nod
  navi.right = gdi
  nod.left = winter
  nod.right = dva
  dva.left = mr_robot
  gdi.left = ghost
  gdi.right = jarvis
  hal.root = navi

  actual = hal.contains(8)
  assert actual == False


def test_bst_contains_true():
  hal = BinarySearchTree()
  jarvis = Node(9)
  mr_robot = Node(3) 
  dva = Node(4) 
  navi = Node(5) 
  gdi = Node(7) 
  nod = Node(2) 
  ghost = Node(6) 
  winter = Node(1) 
  navi.left = nod
  navi.right = gdi
  nod.left = winter
  nod.right = dva
  dva.left = mr_robot
  gdi.left = ghost
  gdi.right = jarvis
  hal.root = navi 

  actual = hal.contains(6)
  assert actual == True


def test_add_empty_bst():
  hal = BinarySearchTree()
  assert hal.root == None
  hal.add(18)
  assert hal.root.value == 18


def test_add_less_root():
  hal = BinarySearchTree()
  hal.add(18)
  hal.add(9)
  assert hal.root.value == 18
  assert hal.root.left.value == 9


def test_add_more_root():
  hal = BinarySearchTree()
  hal.add(18)
  hal.add(27)
  assert hal.root.value == 18
  assert hal.root.right.value == 27


def test_add_less_root_more_child():
  hal = BinarySearchTree()
  hal.add(18)
  hal.add(9)
  hal.add(12)
  print(f'hal.root.left.value:{hal.root.left.value}')
  assert hal.root.left.right.value == 12

def test_add_more_root_less_child():
  hal = BinarySearchTree()
  hal.add(18)
  hal.add(27)
  hal.add(21)
  assert hal.root.right.left.value == 21

def test_add_duplicate():
  hal = BinarySearchTree()
  hal.add(18)
  hal.add(9)
  with pytest.raises(ValueError) as excinfo:
    hal.add(9)
  assert '9 already exists in BinarySearchTree' in str(excinfo.value)