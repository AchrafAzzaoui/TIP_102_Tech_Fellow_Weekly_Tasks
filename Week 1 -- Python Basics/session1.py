# Tech Fellow Task Instructions  
"""
For each of the problems in `main.py`, write out the UPI solution by answering questions 1-4.


During the Implement step, add a commented solution to the problems in `main.py`. 

### U - Understand
1. Share 2 questions you would ask to help understand the question:

### P - Plan
2. Write out in plain English what you want to do:
3. Translate each sub-problem into pseudocode:

### I - Implement
4. Translate the pseudocode into Python and share your final answer:


# Template Questions

1. Share 2 questions you would ask to help understand the question:
  <!-- Your answer here -->
  
2. Write out in plain English what you want to do: 
  <!-- Your answer here -->

3. Translate each sub-problem into pseudocode:
  <!-- Your answer here -->

4. Translate each sub-problem into pseudocode:
  <!-- Your answer here -->

5. Translate the pseudocode into Python and share your final answer:
  <!-- Your answer 
here -->

"""

### SESSION 1, VERSION 1

# QUESTION 1: Hunny Hunt
"""


1. Share 2 questions you would ask to help understand the question:

    Q1: Can the input list be of mixed types? (e.g. strings & ints)
    Q2: Can the input list be an empty list?

2. Write out in plain English what you want to do: 

    I will iterate through the indices of the input list, lst, while doing an
    equality check between each list element at a given index, idx and the 
    target element, target. If this comparison returns True, I will immeadiately return
    the current index. If the loop terminates without this condition ever being rendered
    True, I will return -1.

3. Translate each sub-problem into pseudocode:

    Only one component to this problem -- linearly searching for an element in a sequence.
    Subproblem 1: Find the index of an element in an array, if present.

        for idx 0, 1, ....., length arr - 1
            if arr[idx] equals target
                return idx
4. Translate the pseudocode into Python and share your final answer:
    def linear_search(lst, target):
        for idx in range(len(lst)):
            if lst[idx] == target:
                return idx
        return -1


"""


# Question 2: Bouncy, Flouncy, Trouncy, Pouncy

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Are operations case sensitive?
    Q2: What should happen in the case that we receive an invalid operation -- no effect, or throw an error?

2. Write out in plain English what you want to do:

    I will initialize a local variable tigger, which will be an int set to 1. I will also initialize
    two lists with the string names of the operations that are meant to increment and decrement the value
    of our variable tigger. I will then iterate through every element in the operations argument, check 
    whether its in the increment operations list or decrement operations list, and increment or decrement
    the value of tigger accordingly. Then, I will return the value of tigger at the end of the function 
    after the loop terminates.

3. Translate each sub-problem into pseudocode:

    Only one component to this problem: -- Incrementing or decrementing the value of tigger based on the 
    operations in the operations list.
    
    Subproblem 1: Change the value of tigger based on the specified operations.

        for op op1, op2, ...., op n-1 in operations
            if op in increment_ops
                tigger = tigger + 1
            else if op in decrement_ops
                tigger = tigger - 1

4. Translate the pseudococde into Python and share your final answer:
    def final_value_after_operations(operations):
        tigger = 1
        increment_ops = ["bouncy", "flouncy"]
        decrement_ops = ["trouncy", "pouncy"]

        for op in operations:
            if op in increment_ops:
                tigger += 1
            elif op in decrement_ops:
                tigger -= 1
        return tigger


"""


# Question 3: T-I-Double Guh-Er II

"""

1. Share 2 questions you would ask to help understand the question:
    Q1: Should we remove the substrings in a specific order, or does the order not matter?
    Q2: If multiple substrings overlap (like "tiger" containing both "t", "i", and "er"), 
        how should we handle the removal process?

2. Write out in plain English what you want to do:
    I will iterate through each substring that needs to be removed ("t", "i", "gg", "er") 
    and for each one, I'll search through the current version of the word to find all instances 
    of that substring in a case-insensitive manner. When found, I'll remove it by keeping the 
    portions of the string before and after the substring. I'll continue this process until 
    no more instances of the current substring can be found, then move on to the next substring.

3. Translate each sub-problem into pseudocode:
    Only one component to this problem: Removing substrings from a string in a case insensitive manner.
    Subproblem 1: Remove specific substrings from a word in a case-insensitive manner
    
    result = word
    for each substr in substrs:
        create lowercase copy of result to search in
        while substr exists in lowercase copy:
            find index of substr in lowercase copy
            remove substr from result at that index
            update lowercase copy
       

4. Translate the pseudococde into Python and share your final answer:
    def tiggerfy(word):
        substrs = ["t", "i", "gg", "er"]
        result = word
        for substr in substrs:
            temp = result.lower()
            while substr in temp:
                index = temp.find(substr)
                result = result[:index] + result[index + len(substr):]
                temp = result.lower()

        return result



"""

# Question 4: Non-decreasing Array

"""

1. Share 2 questions you would ask to help understand the question:
  Q1: Does an empty list qualify as a non-decreasing sequence?
  Q2: Is it enough to just count the number of decreases, or do we need to check if making a single 
      modification can actually fix the array?
  
2. Write out in plain English what you want to do: 
  I will track the number of places where the array is decreasing (where nums[i] > nums[i+1]).
  When I find such a place, I need to decide which element to modify - either nums[i] or nums[i+1].
  If I've already found a decreasing place before, I'll return False since we can only make one change.
  For each decreasing pair, I'll determine the best element to modify by checking if modifying nums[i]
  down or nums[i+1] up would maintain the non-decreasing property relative to adjacent elements.
  
3. Translate each sub-problem into pseudocode:
  Subproblem 1: Find and fix decreasing elements in the array
  
    count = 0
    for i from 0 to length of nums - 2:
        if nums[i] > nums[i+1]:
            if count is already 1:
                return False
            increment count
            
            if i > 0 and nums[i-1] > nums[i+1]:
                set nums[i+1] = nums[i]  # Need to increase nums[i+1]
            else:
                set nums[i] = nums[i+1]  # Can decrease nums[i]
    
    return True
        
4. Translate the pseudocode into Python and share your final answer:
    def non_decreasing(nums):
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if count == 1:
                    return False
                count += 1
                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]  # Modify nums[i+1] instead
                else:
                    nums[i] = nums[i + 1]  # Modify nums[i]
        return True


"""

# QUESTION 5: Missing Clues

"""
1. Share 2 questions you would ask to help understand the question:

    Q1: Can the clues list be unsorted, or is it guaranteed to be sorted already?
    Q2: Should we return each missing number as a separate range like [x, x], or group all consecutive missing numbers?

2. Write out in plain English what you want to do:

    I will first sort the clues array to make sure it's in order. Then, I will walk through the clues while maintaining a pointer called `prev`, initialized to `lower - 1`. For each number `curr` in the clues (plus one extra step after, where `curr = upper + 1`), I will check whether the range between `prev` and `curr` contains any missing numbers. If the gap is 2 or more, I will add the range `[prev + 1, curr - 1]` to my result. This way I can collect all the missing numbers in the shortest list of sorted ranges.

3. Translate each sub-problem into pseudocode:

    Only one component to this problem -- walking through the sorted clues and identifying missing number ranges.
    Subproblem 1: Detect gaps between adjacent boundaries and collect missing ranges accordingly.

        result = []
        prev = lower - 1
        for curr in sorted clues concatenated with [upper + 1]:
            if curr - prev >= 2:
                append [prev + 1, curr - 1] to result
            prev = curr


4. Translate the pseudocode into Python and share your final answer:

    def find_missing_clues(clues, lower, upper):
        result = []
        prev = lower - 1
        for curr in sorted(clues) + [upper + 1]:
            if curr - prev >= 2:
                result.append([prev + 1, curr - 1])
            prev = curr
        return result
"""
