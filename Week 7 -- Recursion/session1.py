# Problem 1: Counting the layers of a sandwich

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: What should we return if the sandwich list is empty?
   Q2: Are we counting the total number of elements in the sandwich, or something else?

2. Write out in plain English what you want to do: 

   I want to count the total number of layers (elements) in the sandwich list using recursion.
   My base case will be when the sandwich has only one element - I'll return 1.
   For the recursive case, I'll return 1 (for the current layer) plus the count of layers
   in the rest of the sandwich.

3. Translate each sub-problem into pseudocode:

   Base case: If sandwich has only 1 element, return 1
   Recursive case: Return 1 + count_layers(rest of sandwich)

   if length of sandwich == 1 then
       return 1
   else
       return 1 + count_layers(sandwich[1:])

4. Translate the pseudocode into Python and share your final answer:

   def count_layers(sandwich):
       if len(sandwich) == 1:
           return 1  # Fixed: should return 1, not len(sandwich)
       else:
           return 1 + count_layers(sandwich[1:])  # Fixed: should slice from index 1
"""

# Problem 2: Reversing Deli Orders

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: Should we preserve the original spacing between words, or use single spaces?
   Q2: What should we return if the orders string is empty?

2. Write out in plain English what you want to do: 

   I want to reverse the order of words in the orders string using recursion.
   I'll split the string into words, then use recursion to reverse them.
   My base case will be when there's only one word - I'll return that word.
   For the recursive case, I'll recursively reverse the rest of the words and 
   append the first word to the end.

3. Translate each sub-problem into pseudocode:

   Split orders into words
   Base case: If only one word, return that word
   Recursive case: reverse_orders(rest of words) + " " + first word

   words <- split orders by spaces
   if length of words == 1 then
       return words[0]
   else
       return reverse_orders(join words[1:]) + " " + words[0]

4. Translate the pseudocode into Python and share your final answer:

   def reverse_orders(orders):
       words = orders.split()
       if len(words) == 1:
           return words[0]
       else:
           return reverse_orders(" ".join(words[1:])) + " " + words[0]
"""

# Problem 3: Sharing the Coffee

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: Are we allowed to modify the coffee array in place, or should we work with a copy?
   Q2: What should we return if n is 0 or negative?

2. Write out in plain English what you want to do: 

   I want to check if we can distribute all coffee amounts evenly among n people using recursion.
   My base case will be when there's only one coffee amount left - I'll check if it's divisible by n.
   For the recursive case, if the current amount is divisible by n, I'll continue with the rest.
   If not, I'll add the current amount to the next amount (combining cups) and recurse.

3. Translate each sub-problem into pseudocode:

   Base case: If only one coffee amount, check if divisible by n
   Recursive case: If current amount divisible by n, check rest
                  Otherwise, combine with next amount and check rest

   if length of coffee == 1 then
       return coffee[0] % n == 0
   else
       if coffee[0] % n == 0 then
           return can_split_coffee(coffee[1:], n)
       else
           coffee[1] += coffee[0]
           return can_split_coffee(coffee[1:], n)

4. Translate the pseudocode into Python and share your final answer:

   def can_split_coffee(coffee, n):
       if len(coffee) == 1:
           return coffee[0] % n == 0
       else:
           if coffee[0] % n == 0:
               return can_split_coffee(coffee[1:], n)
           else:
               coffee[1] += coffee[0]
               return can_split_coffee(coffee[1:], n)
"""

# Problem 4: Super Sandwich

"""
1. Share 2 questions you would ask to help understand the question:

   Q1: Should we alternate elements from both lists, or merge in some other pattern?
   Q2: What should we return if both input lists are empty?

2. Write out in plain English what you want to do: 

   I want to merge two linked lists by alternating their elements using recursion.
   My base cases will handle when one or both lists are empty.
   For the recursive case, I'll take the first node from sandwich_a, point it to 
   the first node of sandwich_b, then recursively merge the rest of sandwich_a 
   with the rest of sandwich_b.

3. Translate each sub-problem into pseudocode:

   Base cases: 
   - If both lists empty, return None
   - If sandwich_a empty, return sandwich_b
   - If sandwich_b empty, return sandwich_a
   
   Recursive case: Connect sandwich_a to sandwich_b, then merge rest

   if not sandwich_a and not sandwich_b then
       return None
   elif not sandwich_a then
       return sandwich_b
   elif not sandwich_b then
       return sandwich_a
   else
       next_a <- sandwich_a.next
       sandwich_a.next <- sandwich_b
       sandwich_b.next <- merge_orders(next_a, sandwich_b.next)
       return sandwich_a

4. Translate the pseudocode into Python and share your final answer:

   def merge_orders(sandwich_a, sandwich_b):
       if not sandwich_a and not sandwich_b:
           return None
       elif not sandwich_a:
           return sandwich_b
       elif not sandwich_b:
           return sandwich_a
       else:
           next_a = sandwich_a.next
           sandwich_a.next = sandwich_b
           sandwich_b.next = merge_orders(next_a, sandwich_b.next)
           return sandwich_a
"""


# Problem 5: Super Sandwich II.
"""
I prefer the iterative solution because it has O(1) space complexity, while the recursive solution uses O(min(n,m)) space due to the call stack.
 Both have the same time complexity, but the iterative approach is more memory efficient and won't cause stack overflow issues with large linked lists.
"""