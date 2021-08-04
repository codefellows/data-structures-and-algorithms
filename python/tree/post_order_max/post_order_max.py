from tree.tree import Node, BinaryTree

#Find the max value in a binary tree using post order. Make it a single function.

def postOrderMaxVal(b_tree, max=[0]):
  if not b_tree:
    return
  else:
    postOrderMaxVal(b_tree.left, max)
    postOrderMaxVal(b_tree.right, max)
    print(f'b_tree.value is {b_tree.value}')
    if b_tree.value > max[0]:
      max[0] = b_tree.value
      print(f'b_tree greater than comparison is {max[0]}')
  return max[0]