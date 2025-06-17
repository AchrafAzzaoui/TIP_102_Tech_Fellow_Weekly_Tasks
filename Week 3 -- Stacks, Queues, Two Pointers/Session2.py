### SESSION 2, VERSION 1, Architecture Problem Set

# QUESTION 1: Blueprint Approval Process
"""
1. Share 2 questions you would ask to help understand the question:

    Q1: Can the blueprint complexities have duplicates?
    Q2: Is it guaranteed that all inputs are integers?

2. Write out in plain English what you want to do:

    I will simulate the blueprint approval process by inserting all blueprint
    complexity values into a min-heap so that simpler blueprints are always processed first.
    I’ll then pop from the heap and add each to the result list in sorted order.

3. Translate each sub-problem into pseudocode:

    Subproblem 1: Insert all blueprint complexities into a heap
        for blueprint in blueprints:
            insert blueprint into heap

    Subproblem 2: Pop from heap into result list
        while heap is not empty:
            pop min blueprint and append to result list

4. Translate the pseudocode into Python and share your final answer:
"""
import heapq
def blueprint_approval(blueprints):
    heap = []
    heapq.heapify(heap)
    for blueprint in blueprints:
        heapq.heappush(heap, blueprint)
    correct_order_blueprints = []
    while heap:
        correct_order_blueprints.append(heapq.heappop(heap))
    return correct_order_blueprints


# QUESTION 2: Build the Tallest Skyscraper
"""
1. Share 2 questions you would ask to help understand the question:

    Q1: Can multiple skyscrapers be started consecutively if the condition fails repeatedly?
    Q2: Do floor heights include duplicates or negative values?

2. Write out in plain English what you want to do:

    I will iterate through the floor heights, simulating the stacking process.
    If the next floor can't be stacked due to being taller than the current top,
    I will start a new skyscraper and clear the stack.

3. Translate each sub-problem into pseudocode:

    Subproblem 1: Traverse each floor height
        for floor in floors:
            if floor can't be stacked on current:
                increment skyscraper count
                reset stack
            push floor to stack

4. Translate the pseudocode into Python and share your final answer:
"""
def build_skyscrapers(floors):
    num_skyscrapers = 1
    stack = []

    for floor_h in floors:
        if stack and floor_h > stack[-1]:
            num_skyscrapers += 1
            stack.clear()
        stack.append(floor_h)
    return num_skyscrapers


# QUESTION 3: Dream Corridor Design
"""
1. Share 2 questions you would ask to help understand the question:

    Q1: Can the two chosen segments be adjacent or must they be separated?
    Q2: Is the goal always to maximize the product of distance and min segment height?

2. Write out in plain English what you want to do:

    I will use the two-pointer technique. At each step, calculate the area
    between the segments at the pointers. I will keep the larger segment
    and move the pointer pointing to the smaller one inward.

3. Translate each sub-problem into pseudocode:

    Subproblem 1: Initialize pointers and max_area
        left <- 0, right <- len(segments) - 1, max_area <- 0

    Subproblem 2: Compare area and move pointer
        while left < right:
            area <- (right - left) * min(segments[left], segments[right])
            max_area <- max(max_area, area)
            if segments[left] < segments[right]:
                left += 1
            else:
                right -= 1

4. Translate the pseudocode into Python and share your final answer:
"""
def max_corridor_area(segments):
    l = 0
    r = len(segments) - 1
    max_area = 0
    while l < r:
        area = (r - l) * min(segments[r], segments[l])
        max_area = max(max_area, area)
        if segments[l] >= segments[r]:
            r -= 1
        else:
            l += 1
    return max_area


# QUESTION 4: Dream Building Layout
"""
1. Share 2 questions you would ask to help understand the question:

    Q1: Is the input always balanced in number of '[' and ']'?
    Q2: Do we need to output the balanced string or just count the swaps?

2. Write out in plain English what you want to do:

    I will track the balance of brackets while scanning the string.
    If the balance ever dips negative, I track the minimum imbalance.
    The number of swaps needed is the ceiling of half the absolute minimum imbalance.

3. Translate each sub-problem into pseudocode:

    Subproblem 1: Track balance and min_balance
        balance <- 0, min_balance <- 0
        for char in s:
            if char == '[':
                balance += 1
            else:
                balance -= 1
            min_balance <- min(min_balance, balance)

    Subproblem 2: Compute swaps needed
        return ceil(abs(min_balance) / 2)

4. Translate the pseudocode into Python and share your final answer:
"""
import math

def min_swaps(s):
    balance = 0
    min_balance = 0
    for char in s:
        if char == "[":
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)
    return math.ceil(abs(min_balance) / 2)


# QUESTION 5: Designing a Balanced Room
"""
1. Share 2 questions you would ask to help understand the question:

    Q1: Are all non-parenthesis characters guaranteed to be lowercase letters?
    Q2: Are we allowed to return any valid balanced string, or must it be the lexicographically smallest?

2. Write out in plain English what you want to do:

    I will use a stack to track unmatched '(' characters and a set to store invalid ')' positions.
    After scanning the string, I will remove all unmatched indices from the original string.

3. Translate each sub-problem into pseudocode:

    Subproblem 1: Identify unmatched parentheses
        for index, char in s:
            if char == '(':
                push index to stack
            else if char == ')':
                if stack is not empty:
                    pop stack
                else:
                    add index to invalid set

    Subproblem 2: Add remaining stack indices to invalid set
        for index in stack:
            add index to invalid set

    Subproblem 3: Reconstruct final string
        result <- join all chars in s where index not in invalid set

4. Translate the pseudocode into Python and share your final answer:
"""
def make_balanced_room(s):
    stack = []
    indices_to_remove = set()

    for index, char in enumerate(list(s)):
        if char == "(":
            stack.append(index)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                indices_to_remove.add(index)
    
    for remaining_open_char in stack:
        indices_to_remove.add(remaining_open_char)
    
    remaining_chars = [char for index, char in enumerate(list(s)) if index not in indices_to_remove]
    result_str = "".join(remaining_chars)
    return result_str


