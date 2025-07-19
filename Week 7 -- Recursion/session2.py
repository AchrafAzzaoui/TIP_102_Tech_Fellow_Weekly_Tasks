# Problem 1: Find Millenium Falcon Part I

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: Is the inventory array guaranteed to be sorted?
   Q2: What should we return if the inventory is empty?

2. Write out in plain English what you want to do: 

   I want to search for a specific part_id in a sorted inventory using binary search recursion.
   My base case will be when the inventory is empty - I'll return False.
   For the recursive case, I'll find the middle element and compare it to the target.
   If the target is smaller, I'll search the left half. If larger, I'll search the right half.
   If equal, I'll return True.

3. Translate each sub-problem into pseudocode:

   Base case: If inventory is empty, return False
   Recursive case: Compare target with middle element and search appropriate half

   if length of inventory == 0 then
       return False
   mid_idx <- length of inventory // 2
   mid_val <- inventory[mid_idx]
   if part_id < mid_val then
       return check_stock(inventory[:mid_idx], part_id)
   elif part_id > mid_val then
       return check_stock(inventory[mid_idx + 1:], part_id)
   else
       return True

4. Translate the pseudocode into Python and share your final answer:

   def check_stock(inventory, part_id):
       if len(inventory) == 0:
           return False
       mid_idx = len(inventory) // 2 
       mid_val = inventory[mid_idx]

       if part_id < mid_val:
           return check_stock(inventory[:mid_idx], part_id)
       elif part_id > mid_val:
           return check_stock(inventory[mid_idx + 1: ], part_id)
       else:
           return True
"""

# Problem 2: Find Millenium Falcon Part II

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: Should we maintain the same functionality as the recursive version?
   Q2: How do we handle the case when the element is not found?

2. Write out in plain English what you want to do: 

   I want to implement the same binary search functionality but using iteration instead of recursion.
   I'll use two pointers (left and right) to track the current search range.
   In each iteration, I'll calculate the middle index and compare with the target.
   I'll update the pointers based on the comparison until I find the target or exhaust the search space.

3. Translate each sub-problem into pseudocode:

   Initialize left and right pointers
   While search space is valid, compare middle with target and update pointers

   l <- 0
   r <- length of inventory - 1
   while l <= r do
       mid_idx <- (l + r) // 2
       mid_val <- inventory[mid_idx]
       if part_id < mid_val then
           r <- mid_idx - 1
       elif part_id > mid_val then
           l <- mid_idx + 1
       else
           return True
   return False

4. Translate the pseudocode into Python and share your final answer:

   def check_stock(inventory, part_id):
       l = 0
       r = len(inventory) - 1
       while l <= r:  # Fixed: should be <= not 
           mid_idx = (l + r) // 2
           mid_val = inventory[mid_idx]
           if part_id < mid_val:
               r = mid_idx - 1
           elif part_id > mid_val:
               l = mid_idx + 1
           else:
               return True
       return False
"""

# Problem 3: Find First and Last Frequency Positions

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: What should we return if the target_code is not found in the array?
   Q2: Should we find all occurrences or just the first and last positions?

2. Write out in plain English what you want to do: 

   I want to find the first and last positions of a target code in a sorted array using binary search.
   I'll use a recursive helper function that searches for the target and updates a tuple with the range.
   When I find the target, I'll update the range and continue searching both left and right sides
   to find all occurrences and determine the full range.

3. Translate each sub-problem into pseudocode:

   Initialize result tuple to (-1, -1)
   Use recursive binary search that updates range when target is found

   curr_tuple <- (-1, -1)
   function binary_search(l, r):
       if l > r then return
       mid_idx <- (l + r) // 2
       mid_val <- transmissions[mid_idx]
       if target_code < mid_val then
           binary_search(l, mid_idx - 1)
       elif target_code > mid_val then
           binary_search(mid_idx + 1, r)
       else
           update curr_tuple with mid_idx
           binary_search(l, mid_idx - 1)
           binary_search(mid_idx + 1, r)

4. Translate the pseudocode into Python and share your final answer:

   def find_frequency_positions(transmissions, target_code):
       l = 0
       r = len(transmissions) - 1
       curr_tuple = (-1, -1)
       def binary_search(l, r):
           nonlocal curr_tuple
           if l > r:
               return
           mid_idx = (l + r) // 2
           mid_val = transmissions[mid_idx]

           if target_code < mid_val:
               binary_search(l, mid_idx - 1)
           elif target_code > mid_val:
               binary_search(mid_idx + 1, r)
           else:
               if curr_tuple[0] == -1:
                   curr_tuple = (mid_idx, mid_idx)
               else:
                   curr_tuple = (min(curr_tuple[0], mid_idx), max(curr_tuple[1], mid_idx))
               binary_search(l, mid_idx - 1)
               binary_search(mid_idx + 1, r)
       
       binary_search(l, r)
       return curr_tuple
"""

# Problem 4: Smallest Letter Greater Than Target

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: What should we return if no letter is greater than the target?
   Q2: Should we wrap around to the first letter if no greater letter exists?

2. Write out in plain English what you want to do: 

   I want to find the smallest letter that is greater than the target using binary search.
   I'll track the smallest greater letter found so far and its index.
   When I find a letter greater than target, I'll update my result and search left for a potentially smaller one.
   If no greater letter exists, I'll return the first letter (wrap around).

3. Translate each sub-problem into pseudocode:

   Track smallest greater letter and its index
   Use binary search to find the optimal result

   smallest_greater_idx <- infinity
   smallest_greater_letter <- None
   function binary_search(l, r):
       if l > r then
           if smallest_greater_letter is None then
               smallest_greater_letter <- letters[0]
           return
       mid_idx <- (l + r) // 2
       mid_letter <- letters[mid_idx]
       if target < mid_letter then
           if mid_idx < smallest_greater_idx then
               update smallest_greater_idx and smallest_greater_letter
           binary_search(l, mid_idx - 1)
       else
           binary_search(mid_idx + 1, r)

4. Translate the pseudocode into Python and share your final answer:

   def next_greatest_letter(letters, target):
       smallest_greater_idx = float("inf")
       smallest_greater_letter = None
       def binary_search(l, r):
           nonlocal smallest_greater_letter
           nonlocal smallest_greater_idx
           if l > r: 
               if smallest_greater_letter is None:
                   smallest_greater_letter = letters[0]
               return 

           mid_idx = (l + r) // 2
           
           mid_letter = letters[mid_idx]
           if target < mid_letter:
               if mid_idx < smallest_greater_idx:
                   smallest_greater_idx = mid_idx
                   smallest_greater_letter = mid_letter
               binary_search(l, mid_idx - 1)
           else:
               binary_search(mid_idx + 1, r)
       
       binary_search(0, len(letters) - 1)
       return smallest_greater_letter
"""

# Problem 5: Find K Closest Planets

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: Are the planets sorted by distance from some reference point?
   Q2: Should we return exactly k planets or up to k planets?

2. Write out in plain English what you want to do: 

   I want to find k planets closest to a target distance using a two-pointer approach.
   I'll start with the full array and recursively shrink the window by removing the planet
   that is farther from the target distance. I'll continue until I have exactly k planets.
   The helper function will compare the distances of the leftmost and rightmost planets
   and remove the one that's farther away.

3. Translate each sub-problem into pseudocode:

   Define distance function
   Use recursive helper to shrink window to k elements

   function dist(a, b):
       return abs(a - b)
   
   function helper(l, r):
       if (r - l + 1) <= k then
           return (l, r)
       if dist(planets[l], target_distance) > dist(planets[r], target_distance) then
           return helper(l + 1, r)
       else
           return helper(l, r - 1)

4. Translate the pseudocode into Python and share your final answer:

   def find_closest_planets(planets, target_distance, k):
       def dist(a, b):
           return abs(a - b)
       def helper(l, r):
           if (r - l + 1) <= k:
               return (l, r)
           if dist(planets[l], target_distance) > dist(planets[r], target_distance):
               return helper(l + 1, r)
           else:
               return helper(l, r - 1)
       l, r = helper(0, len(planets) - 1)
       return planets[l: r + 1]
"""