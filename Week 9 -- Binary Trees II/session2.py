from collections import deque 

class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root
  
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)






# Problem 1: Creating Cookie Orders from Descriptions

# class TreeNode:
#     def __init__(self, flavor, left=None, right=None):
#         self.val = flavor
#         self.left = left
#         self.right = right

# def build_cookie_tree(descriptions):
#     hashmap = {}

#     for parent_i, child_i, is_left_i in descriptions:
#         if parent_i not in hashmap:
#             hashmap[parent_i] = TreeNode(parent_i)
#         if child_i not in hashmap:
#             hashmap[child_i] = TreeNode(child_i)
        
#         if is_left_i:
#             hashmap[parent_i].left = hashmap[child_i]
#         else:
#             hashmap[parent_i].right = hashmap[child_i]
        
#     return hashmap[descriptions[0][0]]

# descriptions1 = [
#     ["Chocolate Chip", "Peanut Butter", 1],
#     ["Chocolate Chip", "Oatmeal Raisin", 0],
#     ["Peanut Butter", "Sugar", 1]
# ]

# descriptions2 = [
#     ["Ginger Snap", "Snickerdoodle", 0],
#     ["Ginger Snap", "Shortbread", 1]
# ]

# # Using print_tree() function included at top of page
# print_tree(build_cookie_tree(descriptions1))
# print_tree(build_cookie_tree(descriptions2))




# Problem 2: Cookie Sum
# def count_cookie_paths(root, target_sum):

#     def dfs(curr, curr_sum):
#         curr_sum += curr.val
#         if curr_sum > target_sum:
#             return 0
#         elif not curr.left and not curr.right:
#             return 1 if curr_sum == target_sum else 0
#         elif not curr.left:
#             return dfs(curr.right, curr_sum)
#         elif not curr.right:
#             return dfs(curr.left, curr_sum)
#         else:
#             return dfs(curr.left, curr_sum) + dfs(curr.right, curr_sum)


#     return dfs(root, 0)

# cookie_nums = [10, 5, 8, 3, 7, 12, 4]
# cookies1 = build_tree(cookie_nums)

# """
#     8
#    / \
#   4   12
#  / \    \
# 2   6    10
# """
# cookie_nums = [8, 4, 12, 2, 6, None, 10]
# cookies2 = build_tree(cookie_nums)
# print(count_cookie_paths(cookies1, 22)) 
# print(count_cookie_paths(cookies2, 14)) 




# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right


# # Problem 3: Most Popular Cookie Combo
# def most_popular_cookie_combo(root):
#     from collections import defaultdict
#     if not root:
#         return []
#     freq_map = defaultdict(int)
#     {}
#     max_freq = 0

#     def postorder(node):
#         nonlocal max_freq
#         if not node:
#             return 0
#         subtree_sum = postorder(node.left) + postorder(node.right) + node.val
#         freq_map[subtree_sum] += 1
#         max_freq = max(max_freq, freq_map[subtree_sum])
#         return subtree_sum

#     postorder(root)
#     return [subtree_sum for subtree_sum, freq in freq_map.items() if freq == max_freq]
    
        


# cookies1 = TreeNode(5, TreeNode(2), TreeNode(-3))

# """
#        5
#       / \
#      2  -5
# """
# cookies2 = TreeNode(5, TreeNode(2), TreeNode(-5))

# print(most_popular_cookie_combo(cookies1))  
# print(most_popular_cookie_combo(cookies2))  







# Problem 4: Convert Binary Tree of Bakery Orders to Linked List

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def flatten_orders(orders):
#     if not orders:
#         return None
#     old_left = orders.left
#     old_right = orders.right

#     orders.right = flatten_orders(old_left)
#     orders.left = None

#     flattened_right_subtree = flatten_orders(old_right)
#     curr = orders
#     while curr.right:
#         curr = curr.right
#     curr.right = flattened_right_subtree

#     return orders


# items = ["Croissant", "Cupcake", "Bagel", "Cake", "Pie", None, "Blondies"]
# orders = build_tree(items)

# # Using print_tree() function included at the top of page
# print_tree(flatten_orders(orders))




# Problem 5: Check Bakery Order Completeness
# Problem 1: Creating Cookie Orders from Descriptions

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: Are the parent and child values guaranteed to be unique in the descriptions?
   Q2: Is there always exactly one root node (node that appears as child but never as parent)?

2. Write out in plain English what you want to do: 

   I want to build a binary tree from the given parent-child relationships. I'll create
   a dictionary to store all nodes and another to track which nodes are children.
   For each description, I'll create nodes if they don't exist and establish the
   parent-child relationship. Finally, I'll find the root (node that's never a child).

3. Translate each sub-problem into pseudocode:

   Create dictionaries for nodes and children tracking
   Process each description to build relationships
   Find and return the root node

   nodes <- empty dictionary
   children <- empty set
   for each description [parent, child, is_left] do
       create parent and child nodes if not exist
       add child to children set
       if is_left == 1 then
           parent.left <- child
       else
           parent.right <- child
   
   find root (node not in children set)
   return root

4. Translate the pseudocode into Python and share your final answer:

   def build_cookie_tree(descriptions):
       nodes = {}
       children = set()
       
       for parent, child, is_left in descriptions:
           if parent not in nodes:
               nodes[parent] = TreeNode(parent)
           if child not in nodes:
               nodes[child] = TreeNode(child)
           
           children.add(child)
           
           if is_left == 1:
               nodes[parent].left = nodes[child]
           else:
               nodes[parent].right = nodes[child]
       
       for node in nodes:
           if node not in children:
               return nodes[node]
"""

# Problem 2: Cookie Sum

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: Do we only count paths that end at leaf nodes?
   Q2: Should we include paths where intermediate sums equal the target?

2. Write out in plain English what you want to do: 

   I want to count all root-to-leaf paths where the sum equals the target. I'll use
   DFS to explore all paths, keeping track of the current sum. When I reach a leaf,
   I'll check if the sum equals the target. I'll recursively explore both left and
   right subtrees and return the total count.

3. Translate each sub-problem into pseudocode:

   Use DFS to explore all root-to-leaf paths
   Track current sum and count valid paths
   Base case: leaf node with target sum

   function count_paths(node, current_sum):
       if not node then return 0
       current_sum <- current_sum + node.val
       if node is leaf then
           return 1 if current_sum == target_sum else 0
       return count_paths(node.left, current_sum) + count_paths(node.right, current_sum)

4. Translate the pseudocode into Python and share your final answer:

   def count_cookie_paths(root, target_sum):
       def dfs(node, current_sum):
           if not node:
               return 0
           
           current_sum += node.val
           
           if not node.left and not node.right:
               return 1 if current_sum == target_sum else 0
           
           return dfs(node.left, current_sum) + dfs(node.right, current_sum)
       
       return dfs(root, 0)
"""

# Problem 3: Most Popular Cookie Combo

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: Should we return the actual subtree sums or just the count of most frequent sums?
   Q2: How do we handle negative values in the tree?

2. Write out in plain English what you want to do: 

   I want to calculate the sum of each subtree and find which sums appear most frequently.
   I'll use post-order DFS to calculate subtree sums bottom-up, storing frequency counts
   in a dictionary. After calculating all sums, I'll find the maximum frequency and
   return all sums that have that frequency.

3. Translate each sub-problem into pseudocode:

   Use post-order DFS to calculate subtree sums
   Track frequency of each sum
   Return sums with maximum frequency

   freq_map <- empty dictionary
   function calculate_sum(node):
       if not node then return 0
       left_sum <- calculate_sum(node.left)
       right_sum <- calculate_sum(node.right)
       total_sum <- node.val + left_sum + right_sum
       increment freq_map[total_sum]
       return total_sum
   
   find max frequency and return corresponding sums

4. Translate the pseudocode into Python and share your final answer:

   def most_popular_cookie_combo(root):
       from collections import defaultdict
       freq_map = defaultdict(int)
       
       def calculate_sum(node):
           if not node:
               return 0
           
           left_sum = calculate_sum(node.left)
           right_sum = calculate_sum(node.right)
           total_sum = node.val + left_sum + right_sum
           
           freq_map[total_sum] += 1
           return total_sum
       
       calculate_sum(root)
       max_freq = max(freq_map.values())
       return [sum_val for sum_val, freq in freq_map.items() if freq == max_freq]
"""

# Problem 4: Convert Binary Tree of Bakery Orders to Linked List

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: Should we modify the tree in place or create a new structure?
   Q2: Do we need to maintain the original tree structure elsewhere?

2. Write out in plain English what you want to do: 

   I want to flatten the binary tree into a linked list following preorder traversal.
   I'll use recursion to process the tree. For each node, I'll recursively flatten
   the left and right subtrees, then connect them in preorder sequence: current node
   points to flattened left subtree, which points to flattened right subtree.

3. Translate each sub-problem into pseudocode:

   Use preorder traversal to flatten tree
   Connect nodes in sequence: root -> left subtree -> right subtree
   Set all left pointers to None

   function flatten(node):
       if not node then return
       flatten(node.left)
       flatten(node.right)
       
       store right subtree
       move left subtree to right
       set left to None
       find end of moved subtree
       connect stored right subtree

4. Translate the pseudocode into Python and share your final answer:

   def flatten_orders(orders):
       if not orders:
           return orders
       
       def flatten(node):
           if not node:
               return
           
           flatten(node.left)
           flatten(node.right)
           
           right_subtree = node.right
           node.right = node.left
           node.left = None
           
           current = node
           while current.right:
               current = current.right
           current.right = right_subtree
       
       flatten(orders)
       return orders
"""

# Problem 5: Check Bakery Order Completeness

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: Should we consider an empty tree as complete?
   Q2: How do we efficiently detect if all nodes in the last level are left-aligned?

2. Write out in plain English what you want to do: 

   I want to check if the binary tree is complete using level-order traversal.
   A complete tree has all levels filled except possibly the last, and the last level
   is filled from left to right. I'll use BFS and track when I encounter the first
   null node. After seeing a null, if I encounter any non-null node, it's not complete.

3. Translate each sub-problem into pseudocode:

   Use BFS to traverse level by level
   Track when first null is encountered
   Return false if non-null appears after null

   queue <- deque with root
   seen_null <- False
   while queue is not empty do
       node <- queue.popleft()
       if node is None then
           seen_null <- True
       else
           if seen_null then return False
           add node.left and node.right to queue
   return True

4. Translate the pseudocode into Python and share your final answer:

   def is_complete(root):
       from collections import deque
       queue = deque()
       queue.append(root)

       seen_null = False

       while queue:
           curr_node = queue.popleft()
           if curr_node is None:
               seen_null = True
               continue
           else:
               if seen_null:
                   return False
               queue.append(curr_node.left)
               queue.append(curr_node.right)
           
       return True
"""