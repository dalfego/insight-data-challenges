"""
Given a binary tree, find its maximum depth
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node

"""
# Constructor to create a new node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def depth_helper(node):
    if not node:
        # Check to see if there are any nodes
        return 0
    else:
        # Check both sides of the tree
        nodes_left = depth_helper(node.left)
        nodes_right = depth_helper(node.right)
        # Look for deepest tree
        depth = max(nodes_left,nodes_right)
        # Add one to look at last node
        depth = depth+1
    return depth

#PLEASE DO NOT CHANGE THIS
def find_max_depth(tree):
	depth = depth_helper(tree)
	return depth



#test cases
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print ("Depth of tree is %d, and the expected result is 3" %(find_max_depth(root),))

if __name__ == "__main__":
    main()

