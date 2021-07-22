import math
import os
import random
import re
import sys
from queue import Queue
#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#
class Node:
    def __init__(self, index, depth):
        self.index = index
        self.left = None
        self.right = None
        self.depth = depth
        
def create_binary_tree(indices):
    q = Queue() # Using queue to create tree BFS
    root = Node(1, 1) # Root node is always index 1 and at depth 1
    max_depth = 1 # Variable to keep track of max depth of tree
    q.put(root) # Initialise queue with root
    
    # Iterate through indices and add left and
    # right nodes to tree. Build tree iteratively
    for left, right in indices:
        current_node = q.get() # Remove and return an item from the queue.
        if left != -1:
            leftNode = Node(left, current_node.depth + 1)
            current_node.left = leftNode
            q.put(leftNode)
        if right != -1:
            rightNode = Node(right, current_node.depth + 1)
            current_node.right = rightNode
            q.put(rightNode)
        # Finally the q is empty, and cur 
        # is at lowest level. Because there 
        # are always [-1, -1]s at the end of 
        # the indexes
        max_depth = current_node.depth
    return (root, max_depth)
    
def traverse_inorder(current_node, traversal):
    if current_node.left:
        traverse_inorder(current_node.left, traversal)
    traversal.append(current_node.index)
    if current_node.right:
        traverse_inorder(current_node.right, traversal)

def swap_tree(current_node, depths):
    if current_node.left:
        swap_tree(current_node.left, depths)
    if current_node.right:
        swap_tree(current_node.right, depths)
    if current_node.depth in depths:
        current_node.left, current_node.right = current_node.right, current_node.left
    return current_node

def swapNodes(indexes, queries):
    # Write your code here
    sys.setrecursionlimit(1500) # Change the recursion limit
    binary_tree, max_depth = create_binary_tree(indexes)
    ret = [] # List to store return values
    
    # Iterate through the queries
    for k in queries:
        indices_to_query = []
        depths = [x for x in range(1, max_depth + 1) if x % k == 0]
        root = swap_tree(binary_tree, depths)
        traverse_inorder(root, indices_to_query)
        ret.append(indices_to_query)
    return ret