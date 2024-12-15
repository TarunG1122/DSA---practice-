############# pree order traversal with recurson and stacks

#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# def preorder_recursive(root):
#     result = []
#
#     def traversal(node):
#
#         result.append(node.val)
#         if node.left:
#             traversal(node.left)
#         if node.right:
#             traversal(node.right)
#
#     traversal(root)
#     return result
#
# # Example binary tree:
# #        1
# #         \
# #          2
# #         /
# #        3
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
#
# # Preorder traversal
# print(preorder_recursive(root))  # Output: [1, 2, 3]


######## stacks
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# def preorder_stack(root):
#     if not root:
#         return []
#
#     stack = [root]
#     result = []
#
#     while stack:
#
#         node = stack.pop()
#         result.append(node.val)
#
#         if node.right:
#             stack.append(node.right)
#         if node.left:
#             stack.append(node.left)
#     return result
# # Example binary tree:
# #        1
# #      /   \
# #     2     3
# #    / \
# #   4   5
# root = TreeNode(1)
# root.left = TreeNode(2, TreeNode(4), TreeNode(5))
# root.right = TreeNode(3)
#
# # Preorder traversal
# print(preorder_stack(root))  # Output: [1, 2, 4, 5, 3]
#
####################################################################################################
###################################################################################

### inorder traversal


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# # Construct the tree
# root = TreeNode(1)
# root.left = TreeNode(2, TreeNode(4), TreeNode(5))
# root.right = TreeNode(3)
#
# # Inorder Traversal Function
# def inorder_traversal(node):
#
#     if node is None:
#         return []
#
#     return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
#
#
#
#
# # Call the function and print the result
# print(inorder_traversal(root))


### stacks
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# # Construct the tree
# root = TreeNode(1)
# root.left = TreeNode(2, TreeNode(4), TreeNode(5))
# root.right = TreeNode(3)
#
#
# # Iterative Inorder Traversal Function
# def iterative_inorder_traversal(node):
#     stack = []  # To keep track of nodes
#     result = []  # To store the inorder traversal
#     current = node
#
#     while stack or current:
#         # Traverse the left subtree
#         while current:
#             stack.append(current)
#             current = current.left
#
#         # Visit the node
#         current = stack.pop()
#         result.append(current.val)
#
#         # Traverse the right subtree
#         current = current.right
#
#     return result
#
#
# # Call the function and print the result
# print(iterative_inorder_traversal(root))

###########################################################################################
########################################################################################

### post order



# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# # Construct the tree
# root = TreeNode(1)
# root.left = TreeNode(2, TreeNode(4), TreeNode(5))
# root.right = TreeNode(3)

# # Recursive Post-order Traversal
# def post_order_recursive(node):
#     if node is None:
#         return
#     post_order_recursive(node.left)  # Visit left subtree
#     post_order_recursive(node.right) # Visit right subtree
#     print(node.val, end=" ")         # Visit root node
#
# # Example Usage
# print("Recursive Post-order Traversal:")
# post_order_recursive(root)

# Iterative Post-order Traversal
# def post_order_iterative(node):
#     if not node:
#         return
#     stack, output = [node], []
#     while stack:
#         current = stack.pop()
#         output.append(current.val)  # Visit the node
#         if current.left:
#             stack.append(current.left)  # Push left child
#         if current.right:
#             stack.append(current.right)  # Push right child
#     # Reverse the output to get the post-order sequence
#     print(" ".join(map(str, output[::-1])))
#
# # Example Usage
# print("\nIterative Post-order Traversal:")
# post_order_iterative(root)


###################################################################################
##########################################################

### level order traversal
# #
# from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# # Construct the tree
# root = TreeNode(1)
# root.left = TreeNode(2, TreeNode(4), TreeNode(5))
# root.right = TreeNode(3)
#
# def level_order_traversal(root):
#
#     if not root:
#         return []
#
#     result = []
#
#     queue = deque([root])
#
#     while queue:
#
#         level_size = len(queue)
#
#         level = []
#
#         for _ in range(level_size):
#             node = queue.popleft()
#             level.append(node.val)
#
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#
#         result.append(level)
#
#     return len(result)
#
#
# traversal_result = level_order_traversal(root)
# print(traversal_result)



###############################################################################################3
#######################################################################################


### max depth of binary tree

#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# # Construct the tree
# root = TreeNode(1)
# root.left = TreeNode(2, TreeNode(4), TreeNode(5))
# root.right = TreeNode(3)


# def max_depth_binary_tree(node):
#
#     if node is None:
#         return 0
#
#     return 1 + max(max_depth_binary_tree(node.left),max_depth_binary_tree(node.right))
#
#
#
# print(max_depth_binary_tree(root))


########################################################################################################
##########################################################################################################

############# check for balanneced binary tree

#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# def isBalanced(root):
#     def checkHeight(node):
#         if not node:
#             return 0
#
#         left_height = checkHeight(node.left)
#
#         right_height = checkHeight(node.right)
#
#         if abs(left_height- right_height) > 1 or left_height == -1 or right_height == -1:
#             return -1
#
#
#         return 1 + max(left_height,right_height)
#
#     return checkHeight(root) != -1
#
#
# # Example Usage
# if __name__ == "__main__":
#     # Creating a balanced tree
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.left.left = TreeNode(4)
#     root.left.right = TreeNode(5)
#     root.right.right = TreeNode(6)
#
#     print(isBalanced(root))  # Output: True


###################################################################################################
###########################################################################################

### diameter of a binary tree
#
# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right
#
#
# def diameter_of_binary_tree(root):
#     def height_and_diameter(node):
#         nonlocal max_diameter
#         if not node:
#             return 0
#
#         # Calculate the height of the left and right subtrees
#         left_height = height_and_diameter(node.left)
#         right_height = height_and_diameter(node.right)
#
#         # Calculate the diameter at the current node
#         current_diameter = left_height + right_height
#         max_diameter = max(max_diameter, current_diameter)
#
#         # Return the height of the current node
#         return 1 + max(left_height, right_height)
#
#     max_diameter = 0
#     height_and_diameter(root)
#     return max_diameter
#
#
# # Example Usage
# # Constructing a binary tree
# #        1
# #       / \
# #      2   3
# #     / \
# #    4   5
# root = TreeNode(1)
# root.left = TreeNode(2, TreeNode(4), TreeNode(5))
# root.right = TreeNode(3)
#
# print(diameter_of_binary_tree(root))  # Output: 3

##########################################################################################################
#############################################################################################

#### maximum path sum

#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def maxPathSum(self, root: TreeNode) -> int:
#         # Initialize a variable to store the global maximum path sum
#         self.max_sum = float('-inf')
#
#         # Helper function to calculate maximum gain for each node
#         def max_gain(node):
#
#             if not node:
#                 return 0
#
#             left_max = max(max_gain(node.left),0)
#             right_max = max(max_gain(node.right), 0)
#
#             current_path_sum = node.val + left_max + right_max
#
#             self.max_sum = max(self.max_sum,current_path_sum)
#
#             return node.val + max(left_max,right_max)
#
#         max_gain(root)
#
#         return self.max_sum
#
#
#
# # Example Usage
# # Create a sample binary tree:
# #        -10
# #        /  \
# #       9   20
# #          /  \
# #         15   7
# root = TreeNode(-10)
# root.left = TreeNode(9)
# root.right = TreeNode(20, TreeNode(15), TreeNode(7))
#
# solution = Solution()
# print(solution.maxPathSum(root))  # Output: 42


###############################################################################################
###############################################################################################
### zig zig traversal
# from collections import deque
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# def zigzag_traversal(root):
#     if not root:
#         return []
#
#     result = []
#     queue = deque([root])
#     left_to_right = True
#
#     while queue:
#         current_level = []
#
#         for _ in range(len(queue)):
#             node = queue.popleft()
#             current_level.append(node.val)
#
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#
#         # Reverse the current level if traversing from right to left
#         if not left_to_right:
#             current_level.reverse()
#
#         result.append(current_level)
#         left_to_right = not left_to_right  # Toggle direction for the next level
#
#     return result
#
# if __name__ == "__main__":
#     # Creating a balanced tree
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.left.left = TreeNode(4)
#     root.left.right = TreeNode(5)
#     root.right.right = TreeNode(6)
#
#     # Perform zig-zag traversal
#     traversal_result = zigzag_traversal(root)
#     print("Zig-Zag Traversal:", traversal_result)


###########################################################################################################
###############################################################################

######## boundary traversal

# class Node:
#     def __init__(self, key):
#         self.data = key
#         self.left = None
#         self.right = None

#
# def print_left_boundary(root, result):
#     if root:
#         if root.left:
#             result.append(root.data)
#             print_left_boundary(root.left, result)
#         elif root.right:
#             result.append(root.data)
#             print_left_boundary(root.right, result)
#
#
# def print_leaves(root, result):
#     if root:
#         print_leaves(root.left, result)
#         if not root.left and not root.right:
#             result.append(root.data)
#         print_leaves(root.right, result)
#
#
# def print_right_boundary(root, result):
#     if root:
#         if root.right:
#             print_right_boundary(root.right, result)
#             result.append(root.data)
#         elif root.left:
#             print_right_boundary(root.left, result)
#             result.append(root.data)
#
#
# def boundary_traversal(root):
#     result = []
#     if not root:
#         return result
#
#     # Add root node to the result (only once)
#     result.append(root.data)
#
#     # Print the left boundary in top-down order
#     print_left_boundary(root.left, result)
#
#     # Print all the leaf nodes
#     print_leaves(root.left, result)
#     print_leaves(root.right, result)
#
#     # Print the right boundary in bottom-up order
#     print_right_boundary(root.right, result)
#
#     return result

#
# # Example usage
# if __name__ == "__main__":
#     # Constructing the binary tree
#     root = Node(20)
#     root.left = Node(8)
#     root.left.left = Node(4)
#     root.left.right = Node(12)
#     root.left.right.left = Node(10)
#     root.left.right.right = Node(14)
#     root.right = Node(22)
#     root.right.right = Node(25)
#
#     # Perform boundary traversal
#     result = boundary_traversal(root)
#     print("Boundary Traversal:", result)


#####################################################################################################################################################
###################################################################################################################################################


########### vertical order traversal


# from collections import defaultdict, deque
#
# def verticalOrderTraversal(root):
#     if not root:
#         return []
#
#     dict_nodes = defaultdict(list)
#
#     result = []
#
#     queue = [(root,0)]
#
#     while queue:
#
#         node,col = queue.pop(0)
#         dict_nodes[col].append(node.val)
#
#         if node.left:
#             queue.append((node.left,col-1))
#         if node.right:
#             queue.append((node.right,col+1))
#
#
#     for k in sorted(dict_nodes.keys()):
#         result.append(dict_nodes[k])
#
#     return result
#
#
#
#
#
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# # Create the binary tree
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20, TreeNode(15), TreeNode(7))
#
# print(verticalOrderTraversal(root))


###############################################################################################
###########################################################################
#### top view of a binary tree
# from collections import deque
#
#
# class Node:
#     def __init__(self, key):
#         self.data = key
#         self.left = None
#         self.right = None
#
#
# def top_view(root):
#     if not root:
#         return []
#
#     hd_map = {}  # Dictionary to store the first node at each horizontal distance
#     queue = deque([(root, 0)])  # Queue for level-order traversal (node, HD)
#
#     result = []
#
#     while queue:
#         node,val = queue.popleft()
#
#         if val not in hd_map:
#             hd_map[val] = node.data
#
#         if node.left:
#             queue.append((node.left,val-1))
#         if node.right:
#             queue.append((node.right,val+1))
#
#
#     for k in sorted(hd_map):
#         result.append(hd_map[k])
#
#     return result
#
#
#
# # Example usage:
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.right = Node(4)
# root.left.right.right = Node(5)
# root.left.right.right.right = Node(6)
#
# print(top_view(root))  # Output: [2, 1, 3, 6]


########################################################################################################'
##############################################################################################

### bottom view of a binary tree
# from collections import deque, defaultdict
#
#
# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right
#
#
# def bottom_view(root):
#     if not root:
#         return []
#
#     # Map to store the bottom-most node for each horizontal distance
#     hd_map = {}
#     # Queue for level-order traversal: stores nodes and their horizontal distance
#     queue = deque([(root, 0)])
#
#     while queue:
#         node, hd = queue.popleft()
#
#         # Update the map with the current node at this horizontal distance
#         hd_map[hd] = node.value
#
#         # Add left and right children to the queue
#         if node.left:
#             queue.append((node.left, hd - 1))
#         if node.right:
#             queue.append((node.right, hd + 1))
#
#     # Extract the bottom view by sorting horizontal distances
#     bottom_view = [hd_map[hd] for hd in sorted(hd_map)]
#     print(hd_map)
#     return bottom_view
#
#
# # Example Usage
# root = TreeNode(20)
# root.left = TreeNode(8)
# root.right = TreeNode(22)
# root.left.left = TreeNode(5)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(25)
# root.left.right.left = TreeNode(10)
# root.left.right.right = TreeNode(14)
#
# print(bottom_view(root))  # Output: [5, 10, 4, 14, 25]

################################################################################################
#######################################################################################################3


### left view
#
# from collections import deque
#
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# def level_order_traversal(root):
#     if not root:
#         return []
#
#     result = []
#     queue = deque([root])
#
#     while queue:
#         level = []
#         level_size = len(queue)
#
#         for _ in range(level_size):
#             node = queue.popleft()
#             level.append(node.val)
#
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#
#         result.append(level[-1])
#
#     return result
#
#
# # Example usage
# root = TreeNode(20)
# root.left = TreeNode(8)
# root.right = TreeNode(22)
# root.left.left = TreeNode(5)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(25)
# root.left.right.left = TreeNode(10)
# root.left.right.right = TreeNode(14)
# #
#
# print(level_order_traversal(root))

#####################################################################################
######################################################################################
############ symmetirical


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# def isSymmetric(root: TreeNode) -> bool:
#     if not root:
#         return True
#
#     def isMirror(t1, t2):
#         if not t1 and not t2:
#             return True
#         if not t1 or not t2:
#             return False
#         return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
#
#     return isMirror(root.left, root.right)

#############################################################################################
#############################################################################################
#
# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right
#
#
# def print_root_to_node_path(root, target):
#     # Helper function to find the path
#     def find_path(node, target, path):
#         if node is None:
#             return False
#
#         # Add current node to path
#         path.append(node.value)
#
#         # If the current node is the target, return True
#         if node.value == target:
#             return True
#
#         # Otherwise, check both subtrees
#         if (find_path(node.left, target, path) or find_path(node.right, target, path)):
#             return True
#
#         # Backtrack if not found in either subtree
#         path.pop()
#         return False
#
#     # Initialize an empty path list and call the helper function
#     path = []
#     if find_path(root, target, path):
#         print("Root to Node Path:", path)
#     else:
#         print("Node not found in the tree")
#
#
# # Example Usage
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
#
# # Find and print the path from root to node with value 5
# print_root_to_node_path(root, 5)


##########################################################################################
########################################################################################

### lowest common ansistors
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# def lowestCommonAncestor(root, p, q):
#     # Base case: if root is None or root is one of the nodes p or q
#     if not root or root == p or root == q:
#         return root
#
#     # Recur on left and right subtrees
#     left = lowestCommonAncestor(root.left, p, q)
#     right = lowestCommonAncestor(root.right, p, q)
#
#     # If p and q are found in different subtrees, root is the LCA
#     if left and right:
#         return root
#
#     # If both p and q are on the left or right, return the non-None node
#     return left if left else right
#
#
# # Example tree
# #        3
# #       / \
# #      5   1
# #     / \ / \
# #    6  2 0  8
# #      / \
# #     7   4
#
# # Creating nodes
# root = TreeNode(3)
# node5 = TreeNode(5)
# node1 = TreeNode(1)
# node6 = TreeNode(6)
# node2 = TreeNode(2)
# node0 = TreeNode(0)
# node8 = TreeNode(8)
# node7 = TreeNode(7)
# node4 = TreeNode(4)
#
# # Building the tree
# root.left = node5
# root.right = node1
# node5.left = node6
# node5.right = node2
# node1.left = node0
# node1.right = node8
# node2.left = node7
# node2.right = node4
#
# # Example 1: Finding LCA of 5 and 1
# p = node5
# q = node1
# lca = lowestCommonAncestor(root, p, q)
# print(f"LCA of {p.val} and {q.val}: {lca.val if lca else 'None'}")  # Expected output: 3
#
# # Example 2: Finding LCA of 6 and 7
# p = node6
# q = node7
# lca = lowestCommonAncestor(root, p, q)
# print(f"LCA of {p.val} and {q.val}: {lca.val if lca else 'None'}")  # Expected output: 5
#
# # Example 3: Finding LCA of 6 and 8
# p = node6
# q = node8
# lca = lowestCommonAncestor(root, p, q)
# print(f"LCA of {p.val} and {q.val}: {lca.val if lca else 'None'}")  # Expected output: 3


#################################################################################################################
###############################################################################################

#### maximimum widht binary tree

#
# from collections import deque
#
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# def maxWidthOfBinaryTree(root):
#     if not root:
#         return 0
#
#     max_width = 0
#     # Queue stores tuples of (node, position)
#     queue = deque([(root, 0)])
#
#     while queue:
#         level_length = len(queue)
#         _, first_pos = queue[0]  # Position of the first node in the level
#         for _ in range(level_length):
#             node, pos = queue.popleft()
#             if node.left:
#                 queue.append((node.left, 2 * pos))
#             if node.right:
#                 queue.append((node.right, 2 * pos + 1))
#         # Last position in the level
#         _, last_pos = queue[-1] if queue else (None, pos)
#         max_width = max(max_width, last_pos - first_pos + 1)
#
#     return max_width
#
# # Example usage:
# # Construct a binary tree
# #          1
# #         / \
# #        3   2
# #       /     \
# #      5       9
# #     /         \
# #    6           7
# root = TreeNode(1)
# root.left = TreeNode(3)
# root.right = TreeNode(2)
# root.left.left = TreeNode(5)
# root.right.right = TreeNode(9)
# root.left.left.left = TreeNode(6)
# root.right.right.right = TreeNode(7)
#
# print(maxWidthOfBinaryTree(root))  # Output: 8


############################################################################################
#########################################################################################

### Children Sum Property in Binary Tree



############################################################################################
#######################################################################################

#### Print all the Nodes at a distance of K in Binary Tree
