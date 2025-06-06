
### SESSION 1, VERSION 1, Advanced Problem Set

# QUESTION 1: Counting Treasure
"""


1. Share 2 questions you would ask to help understand the question:

    Q1: Is the expected time complexity O(n)?
    Q2: What should be returned if there are no k,v pairs in the input hashmap?

2. Write out in plain English what you want to do: 

    I will store an accumulator sum variable, initialized to 0.
    I will pass through the values of the input, treasure_map, and increment
    the accumulator variable by each value sequentially. Then, at the end we will
    return the accumulator variable.


3. Translate each sub-problem into pseudocode:
    Only one component to this problem -- linearly accumulating the sum of the values
    in the dictionary.

    Subproblem 1 -- Find the sum of the values in the dictionary.

    for num_treasure_i num_treasures_1, num_treasures_2, ..., num_treasures_n in values of treasure_map do
        sum_treasures <- sum_treasures + num_treasures_i
 
4. Translate the pseudocode into Python and share your final answer:
    def total_treasures(treasure_map):
        sum_treasures = 0 # initialize accumulator variable
        for curr_treasure_amount in treasure_map.values():
            sum_treasures += curr_treasure_amount
        return sum_treasures

"""

# QUESTION 2: Pirate Message Check

"""
1. Share 2 questions you would ask to help understand the question:

    Q1: Should we throw an exception if we get an input with numeric or special characters,
    or is the input always assumed to be well-formed?
    Q2: Is it possible to do this problem better than O(n) time complexity and O(n) space complexity?

2. Write out in plain English what you want to do: 
    I will create a hashset of the characters in message. I will assume it contains
    only lowercase alphabetical characters and whitespace.

3. Translate each sub-problem into pseudocode:
    Subproblem 1: Creating a set of characters from message
        unique_chars <- set of message
    
    Subproblem 2: Checking if this set accounts for all lowercase alphabetical characters
        discard ' ' from unique_chars, if present
        return length of unique_chars == 26

    
 
4. Translate the pseudocode into Python and share your final answer:

    def can_trust_message(message):
        unique_chars = set(message)
        unique_chars.discard(' ')
        return len(unique_chars) == 26
  
"""


# QUESTION 3: Find All Duplicate Treasure Chests in an Array

"""
1. Share 2 questions you would ask to help understand the question:

    Q1: If we didn't have the constraint that an integer can occur at max twice, how would that have to change our approach? 
    Q2: Is this problem best approached through the use of an auxillary hashset?

2. Write out in plain English what you want to do: 

    I will create an empty set that will track the integers we've encountered
    so far in the chests array. I will also create a list that holds the duplicate elements.
    Then I will iterate through the chests array -- for every integer, I will do a 
    membership check of this element with the set. If it's already been added to the set,
    then I will add it to the duplicate list. Then, I will return the duplicate list after 
    the loop terminates.
    
3. Translate each sub-problem into pseudocode:

    Only one component to this problem: Adding duplicate elements in the array to another list.

    visited <- empty set
    duplicates <- empty list
    for chest in chests do
        if chest in visited then
            append chest to duplicates
        add chest to visited
    return duplicates
    

    
 
4. Translate the pseudocode into Python and share your final answer:
    def find_duplicate_chests(chests):
        visited = set()
        duplicates = []
        for chest in chest:
            if chest in visited:
                duplicates.append(chest)
            else:
                visited.add(chest)
        return duplicates


"""


# QUESTION 4: Booby Trap

"""
1. Share 2 questions you would ask to help understand the question:

    Q1: Do we need two loops, one over the string, and one over a frequency hashmap
    Q2: How should we keep track of not just whether there are two unique frequency values with
    a difference of one between them, but that only one number is as frequent as the max of the two?

2. Write out in plain English what you want to do: 

    I will first store a hashmap that maps each character to its frequency in code.
    Then, I will create a hashset, on which I will add the frequencies in the frequency hashmap.
    Since we are trying to remove exactly one character to make the code balanced, The condition we need
    is that all characters are equal frequency except one character, which occurs exactly one more time
    than the rest of them. Therefore, it's not enough to check that the length of the set of frequencies is 2, 
    we need to store the max once we get to a set length of 2 and return false if the max freq ever occurs again.

    
3. Translate each sub-problem into pseudocode:

    Subproblem 1: Store the frequencies of each character in code in a hashmap

    freqs <- empty hashmap 
    for char char_1, char_2, ..., char_n in code do
        freqs[char] = 1 + 0 if char not in freqs else freqs[char]
    
    Subproblem 2: Check if we have the right conditions to replace exactly one character and create
    a balanced string.

    unique_freqs <- empty set
    for char, freq (char_1, freq_1), (char_2, freq_2), ..., (char_n, freq_n) in freqs do
        if length of unique_freqs == 2 and freq == max in unique_freqs then
            return False
        add char to unique_freqs
        if length of unique_freqs > 2 then
            return False
    
    return True if length of unique_freqs == 2 else False

    
 
4. Translate the pseudocode into Python and share your final answer:

    def is_balanced(code):
        freqs = {}
        for char in code:
            freqs[char] = 1 + freqs.get(char, 0)
        
        unique_freqs = set()
        for char, freq in freqs.items():
            if len(unique_freqs) == 2 and freq == max(unique_freqs):
                return False
            unique_freqs.add(freq)
            if len(unique_freqs) > 2:
                return False
            
        return len(unique_freqs) == 2

"""

# QUESTION 5: Overflowing With Gold

"""
1. Share 2 questions you would ask to help understand the question:

    Q1: Is this the same as the leetcode question two sum?
    Q2: Is this most optimally solved with a hashmap?

2. Write out in plain English what you want to do: 

I will instantiate an empty hashmap that will map values in the gold
amounts array to their indices. I will iterate through index, val pairs in 
the gold amounts array -- in each iteration, I will do a membership test between target
- curr_val and the hashmap. If its present, I will return a list containing the hashmap
val associated with key target-curr_val at index 0, and the curr_idx at index 1. 
Otherwise, I will add the k,v pair curr_val, curr_index to the hashmap.
At the end of the function, I will return an empty array.

    
3. Translate each sub-problem into pseudocode:
    Only one component to this problem: Checking if the difference between 
    any value in the array and the target value is also in the array

    val_2_idx <- empty hashmap
    for idx, val (idx_0, val_1), (idx_1, val_2), ..., (idx_n-1, val_n) in gold_amounts do
        if target - val in val_2_idx then
            return [val_2_idx[target-val], idx]
        else then
            val_2_idx[val] <- idx
    return []
    
 
4. Translate the pseudocode into Python and share your final answer:
    def find_treasure_indices(gold_amounts, target):
        val_2_idx = {}
        for idx, val in enumerate(gold_amounts):
            if target - val in val_2_idx:
                return [val_2_idx[target - val], idx]
            val_2_idx[val] = idx
        return []

"""
