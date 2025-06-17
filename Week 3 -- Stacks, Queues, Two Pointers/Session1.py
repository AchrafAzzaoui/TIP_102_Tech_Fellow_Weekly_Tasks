### SESSION 1, VERSION 1, Standard Problem Set

# QUESTION 1: Post Format Validator
"""
1. Share 2 questions you would ask to help understand the question:

    Q1: What should happen if a closing bracket is encountered when the stack is already empty?
    Q2: Can we assume the input only contains valid bracket characters?

2. Write out in plain English what you want to do:

    I will maintain a stack to store opening brackets.
    Every time I see a closing bracket, I’ll pop from the stack and verify it matches.
    If it doesn’t match or the stack is empty, I will return False.
    At the end, I will return True if the stack is empty, and False otherwise.

3. Translate each sub-problem into pseudocode:

    Subproblem 1: Check for opening brackets
        if char is an opening bracket:
            push to stack

    Subproblem 2: Handle closing brackets
        if char is a closing bracket:
            if stack is empty or stack.pop() does not match:
                return False

    Subproblem 3: Final validity check
        return True if stack is empty, else False

4. Translate the pseudocode into Python and share your final answer:
"""
def is_valid_post_format(posts):
    close_to_open = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in posts:
        if char in close_to_open.values():
            stack.append(char)
        elif char in close_to_open:
            if not stack or stack.pop() != close_to_open[char]:
                return False
    return not stack


# QUESTION 2: Reverse User Comments Queue
"""
1. Share 2 questions you would ask to help understand the question:

    Q1: Are we allowed to use auxiliary data structures like a stack?
    Q2: Should the reversal happen in place or can we return a new list?

2. Write out in plain English what you want to do:

    I will push all the comments to a stack.
    Then, I will pop each comment from the stack into a new list.
    This gives the reversed order.

3. Translate each sub-problem into pseudocode:

    Subproblem 1: Push to stack
        for comment in comments:
            push comment to stack

    Subproblem 2: Pop to reversed list
        while stack is not empty:
            pop from stack and append to reversed list

4. Translate the pseudocode into Python and share your final answer:
"""
def reverse_comments_queue(comments):
    stack = []
    for comment in comments:
        stack.append(comment)

    reversed_comments = []
    while stack:
        reversed_comments.append(stack.pop())

    return reversed_comments


# QUESTION 3: Check Symmetry in Post Titles
"""
1. Share 2 questions you would ask to help understand the question:

    Q1: Should we ignore punctuation and spacing in the symmetry check?
    Q2: Is letter casing relevant or should comparison be case-insensitive?

2. Write out in plain English what you want to do:

    I will use two pointers, one at the start and one at the end of the string.
    I will skip any non-alphanumeric characters.
    I will compare lowercase versions of the remaining characters.
    If all mirrored characters match, return True. Otherwise, return False.

3. Translate each sub-problem into pseudocode:

    Subproblem 1: Skip non-alphanum from both sides
        while l < r and title[l] not alnum:
            l += 1
        while l < r and title[r] not alnum:
            r -= 1

    Subproblem 2: Compare characters
        if lower(title[l]) != lower(title[r]):
            return False

    Subproblem 3: Move pointers inward
        l += 1
        r -= 1

4. Translate the pseudocode into Python and share your final answer:
"""
def is_symmetrical_title(title):
    l, r = 0, len(title) - 1

    while l < r:
        while l < r and not title[l].isalnum():
            l += 1
        while l < r and not title[r].isalnum():
            r -= 1

        if title[l].lower() != title[r].lower():
            return False

        l += 1
        r -= 1

    return True


# QUESTION 4: Engagement Boost
"""
1. Share 2 questions you would ask to help understand the question:

    Q1: Should the result be sorted in non-decreasing order?
    Q2: Is the input guaranteed to be sorted initially?

2. Write out in plain English what you want to do:

    I will use two pointers from both ends of the input array.
    I will compare the absolute values of the numbers.
    The larger square will be placed at the current end of the result array.

3. Translate each sub-problem into pseudocode:

    Subproblem 1: Initialize result array and pointers
        result = array of size n
        left = 0
        right = n - 1
        pos = n - 1

    Subproblem 2: Compare absolute values
        if abs(engagements[left]) > abs(engagements[right]):
            result[pos] = square(engagements[left])
            left += 1
        else:
            result[pos] = square(engagements[right])
            right -= 1
        pos -= 1

4. Translate the pseudocode into Python and share your final answer:
"""
def engagement_boost(engagements):
    n = len(engagements)
    squared_engagements = [0] * n
    left_ptr = 0
    right_ptr = n - 1
    current_position = n - 1

    while left_ptr <= right_ptr:
        left_val = engagements[left_ptr]
        right_val = engagements[right_ptr]

        if abs(left_val) > abs(right_val):
            squared_engagements[current_position] = left_val * left_val
            left_ptr += 1
        else:
            squared_engagements[current_position] = right_val * right_val
            right_ptr -= 1

        current_position -= 1

    return squared_engagements


# QUESTION 5: Content Cleaner
"""
1. Share 2 questions you would ask to help understand the question:

    Q1: Should we only remove pairs of adjacent letters that are the same but opposite case?
    Q2: Can multiple collapses happen after a single pop, or is it one-pass only?

2. Write out in plain English what you want to do:

    I will use a stack to hold valid characters.
    If the current character and the top of the stack are the same letter in opposite cases,
    I will remove the top from the stack. Otherwise, I will push the current character.

3. Translate each sub-problem into pseudocode:

    Subproblem 1: Iterate through each character in post
        for char in post:
            if stack not empty and char cancels with stack top:
                pop stack
            else:
                push char to stack

    Subproblem 2: Construct final result
        return join(stack)

4. Translate the pseudocode into Python and share your final answer:
"""
def clean_post(post):
    stack = []
    for char in post:
        if stack and (
            (stack[-1].isupper() and stack[-1].lower() == char) or
            (char.isupper() and char.lower() == stack[-1])
        ):
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)
