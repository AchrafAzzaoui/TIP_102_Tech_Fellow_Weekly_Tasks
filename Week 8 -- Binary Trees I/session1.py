# Problem 1: Ivy Cutting

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: What should we return if the root is None?
   Q2: Should we include nodes that don't have a right child in our result?

2. Write out in plain English what you want to do: 

   I want to traverse down the right side of a binary tree and collect all the values
   in a list using recursion. My base case will be when the root is None (return empty list)
   or when there's no right child (return just the current value). For the recursive case,
   I'll add the current value to the result and continue with the right child.

3. Translate each sub-problem into pseudocode:

   Base cases: If root is None, return empty list
              If no right child, return list with current value
   Recursive case: Return current value + right_vine of right child

   if not root then
       return []
   elif not root.right then
       return [root.val]
   else
       return [root.val] + right_vine(root.right)

4. Translate the pseudocode into Python and share your final answer:

   def right_vine(root):
       if not root: 
           return []
       elif not root.right:
           return [root.val]
       else: 
           return [root.val] + right_vine(root.right)
"""

# Problem 2: Ivy Cutting II

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: Should this have the same functionality as the recursive version?
   Q2: How do we handle the case when the root is None?

2. Write out in plain English what you want to do: 

   I want to implement the same right vine traversal but using iteration instead of recursion.
   I'll use a current pointer starting at the root and a list to store the sequence.
   I'll iterate while the current node exists, adding its value to the list and
   moving to the right child until I reach the end.

3. Translate each sub-problem into pseudocode:

   Initialize current pointer and result list
   While current node exists, add value and move right

   curr <- root
   right_vine_sequence <- empty list
   while curr do
       append curr.val to right_vine_sequence
       curr <- curr.right
   return right_vine_sequence

4. Translate the pseudocode into Python and share your final answer:

   def right_vine(root):
       curr = root
       right_vine_sequence = []

       while curr:
           right_vine_sequence.append(curr.val)
           curr = curr.right

       return right_vine_sequence
"""

# Problem 3: Pruning Plans

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: What order should we visit the nodes in?
   Q2: Should we return an empty list if the root is None?

2. Write out in plain English what you want to do: 

   I want to perform a post-order traversal of the binary tree using recursion.
   This means I'll visit the left subtree first, then the right subtree, then the root.
   My base case will be when the root is None (return empty list).
   For the recursive case, I'll combine the results from left and right subtrees and add the current value.

3. Translate each sub-problem into pseudocode:

   Base case: If root is None, return empty list
   Recursive case: Visit left, then right, then current node

   if not root then
       return []
   else
       return survey_tree(root.left) + survey_tree(root.right) + [root.val]

4. Translate the pseudocode into Python and share your final answer:

   def survey_tree(root):
       if not root:
           return []
       else:
           return survey_tree(root.left) + survey_tree(root.right) + [root.val]
"""

# Problem 4: Sum Inventory

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: What should we return if the inventory tree is empty?
   Q2: Are all node values guaranteed to be numbers?

2. Write out in plain English what you want to do: 

   I want to calculate the sum of all values in a binary tree using recursion.
   My base case will be when the current node is None (return 0).
   For the recursive case, I'll return the sum of the current node's value plus
   the sums of the left and right subtrees.

3. Translate each sub-problem into pseudocode:

   Base case: If node is None, return 0
   Recursive case: Return current value + sum of left subtree + sum of right subtree

   if not inventory then
       return 0
   return sum_inventory(inventory.left) + sum_inventory(inventory.right) + inventory.val

4. Translate the pseudocode into Python and share your final answer:

   def sum_inventory(inventory):
       if not inventory:
           return 0
       return sum_inventory(inventory.left) + sum_inventory(inventory.right) + inventory.val
"""

# Problem 5: Calculate Yield

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: What operators should we support in the expression tree?
   Q2: How should we handle division by zero?

2. Write out in plain English what you want to do: 

   I want to evaluate an expression tree where leaf nodes contain numbers and
   internal nodes contain operators. I'll use recursion to evaluate the tree.
   My base case will be when the node is None (return 0) or when the node contains a number.
   For the recursive case, I'll check what operator the node contains and apply it
   to the results of evaluating the left and right subtrees.

3. Translate each sub-problem into pseudocode:

   Base case: If root is None, return 0
             If root value is a number, return that number
   Recursive case: Apply operator to results of left and right subtrees

   if not root then
       return 0
   if root.val is number then
       return root.val
   else
       match root.val:
           case "+": return calculate_yield(root.left) + calculate_yield(root.right)
           case "-": return calculate_yield(root.left) - calculate_yield(root.right)
           case "*": return calculate_yield(root.left) * calculate_yield(root.right)
           case "/": return calculate_yield(root.left) / calculate_yield(root.right)

4. Translate the pseudocode into Python and share your final answer:

   def calculate_yield(root):
       if not root:
           return 0
       if isinstance(root.val, (int, float)):
           return root.val
       else:
           match root.val:
               case "+":
                   return calculate_yield(root.left) + calculate_yield(root.right)
               case "-":
                   return calculate_yield(root.left) - calculate_yield(root.right)
               case "*":
                   return calculate_yield(root.left) * calculate_yield(root.right)
               case "/":
                   return calculate_yield(root.left) / calculate_yield(root.right)
"""