# Question 1: Transpose matrix

"""
1. Share 2 questions you would ask to help understand the question:
    Q1: If the matrix is square, should we transpose in place?
    Q2: If the matrix is not square, does this require O(n * m) space?

2. Write out in plain English what you want to do:

    First, I will check if the matrix is square. If the matrix
    is square, I will transpose the matrix in place, by iterating
    through the rows and columns (in that order) and swapping every 
    row i col j element in the upper right triangle with its row j col i counterpart.

    If the matrix is not square, I will create a new matrix. If the original
    matrix is m x n, the new matrix will be n x m. However, at first, I will have 
    a list of n empty lists. Then, I will iterate through each element in the original matrix
    in row-major order, and append each element to the sublist at the index of the current column.

    Finally, I will return the new matrix.

3. Translate each sub-problem into pseudocode:


    Subproblem 1: Transpose the matrix in place if it is square.

        for idx 0, 1, 2, ..., m-1 in matrix
            for idx2 idx + 1, ..., n-1 in matrix
                swap matrix[idx][idx2] with matrix[idx2][idx]
    
    Subproblem 2: Create a new matrix if the original matrix is not square.

        res = list of n empty lists
        for idx 0, 1, 2, ..., m-1 in matrix
            for idx 0, 1, 2, ..., n-1 in matrix
                append matrix[idx][idx] to res[idx]
4. Implement the pseudocode in Python:

    def transpose(matrix):def transpose(matrix):
        if len(matrix) == len(matrix[0]): # square matrix (m == n)
            for i in range(len(matrix)):
                for j in range(i + 1, len(matrix[0])):  # Only swap upper triangle (not including diagonal elements since those are already in the right place)
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            return matrix
        else: # non-square matrix (m != n)
            res = [[] for _ in range(len(matrix[0]))] # n rows, m columns (currenty 0 columns)
            for r in range(len(matrix)):
                for c in range(len(matrix[0])):
                    res[c].append(matrix[r][c])
            return res
                
"""


# Question 2: Two-Pointer Reverse List

"""
1. Share 2 questions you would ask to help understand the question:
    Q1: Is the expected complexity O(n) time, O(1) space?
    Q2: Can I assume that the list is not empty?

2. Write out in plain English what you want to do:

    I will initialize two pointers, one at the first index in the array
    and the other at the end. I will swap the elements at the lower and upper pointers
    in the list, and then increment the lower pointer and decrement the upper pointer.
    I will continue doing this until the lower pointer is no longer less than the upper pointer.
    Then, I will return the same list object that was passed in as an argument, updated in place.

3. Translate each sub-problem into pseudocode:

    Only one component to this problem: Swapping the elements of the array at 
    the corresponding lower and upper pointers, representing the elements old index and
    new index in the reversed list.

    Subproblem 1: Swapping the elements at the lower and upper pointers.

        left <- 0
        right <- length lst - 1
        while left < right
            swap lst[left] with lst[right]
            left <- left + 1
            right <- right - 1
        return lst

4. Implement the pseudocode in Python:

    def reverse_list(lst):
        left = 0 # lower pointer
        right = len(lst) - 1 # upper pointer
        while left < right: # swap elements until pointers meet so we don't do repeated work/swaps
            temp = lst[left] # save value of array element at lower pointer
            lst[left] = lst[right] # replace value at lower pointer with value at upper pointer
            lst[right] = temp # replace value at upper pointer with saved value at lower pointer
            left += 1 # move lower pointer to the right
            right -= 1 # move upper pointer to the left
        return lst
"""

# Question 3: Remove duplicates

"""
1. Share 2 questions you would ask to help understand the question:
    Q1: Is the expected time complexity O(n)?
    Q2: Can we create auxiliary data structures such as a hash set while still modifying the list in place?

2. Write out in plain English what you want to do:

    I will have a left pointer that starts at index 0 that will allow me to keep track
    of how many non-duplicate elements we've confirmed. Then, I will iterate through the list's indices
    starting at index 1. For every element encountered, I will do an equality check between the current element
    and the element at the left pointer index in the array. If they are equal, we will continue to the next element.
    If they are not equal, we will increment the left pointer, set the element at the new left pointer index equal to
    the current element, and then continue to the next element.

    Finally, I will return left pointer + 1 which is the number of unique elements in the list.

3. Translate each sub-problem into pseudocode:

    Only one component to this problem: Iterating through the list and checking for duplicates.

    Subproblem 1: Iterating through the list and checking for duplicates.

        left <- 0
        for idx 1, 2, ..., n-1 in lst
            if lst[idx] != lst[left]
                left <- left + 1
                lst[left] <- lst[idx]

4. Implement the pseudocode in Python:
    def remove_dupes(items):
        l = 0 # left pointer
        for r in range(1, len(items)):
            if items[r] != items[l]: # if the element at the left pointer is not equal to the current element, we have found another unique element.
                l += 1
                items[l] = items[r] # move the unique element to the left pointer index
        return l + 1 # return the number of unique elements

"""


# Question 4: Sort Array by Parity
"""
    1. Share 2 questions you would ask to help understand the question:
    Q1: Is modifying the list in place preferred?
    Q2: Is the expected time complexity O(n)?

    2. Write out in plain English what you want to do:

    I will have two pointers, one at the beginning of the list and one at the end.
    I will swap the elements at the two pointers if the element at the left pointer is odd
    and the element at the right pointer is even. Then, I will increment the left pointer
    and decrement the right pointer. I will continue doing this until the left pointer is
    no longer less than the right pointer.

    Finally, I will return the list.

    3. Translate each sub-problem into pseudocode:

    Only one component to this problem: Swapping the elements at the two pointers.

    Subproblem 1: Swapping the elements at the two pointers.

        left <- 0
        right <- len(nums) - 1
        while left < right
            if nums[left] % 2 == 1 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] % 2 == 0:
                left <- left + 1
            if nums[right] % 2 == 1:
                right <- right - 1
    
    4. Implement the pseudocode in Python:
    def sort_by_parity(nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] % 2 == 1 and nums[right] % 2 == 0: # if the element at the left pointer is odd and the element at the right pointer is even, we swap them.
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] % 2 == 0: # if the element at the left pointer is even, we increment the left pointer.
                left += 1
            if nums[right] % 2 == 1: # if the element at the right pointer is odd, we decrement the right pointer.
                right -= 1
        return nums
"""

# Question 5: Container with the most honey

"""
1. Share 2 questions you would ask to help understand the question:
    Q1:     
    Q2: 

2. Write out in plain English what you want to do:

    I will initialize a max_honey variable to 0. Then, I will have two pointers, one at the beginning of the list and one at the end.
    I will calculate the area of the container formed by the two pointers, and then I will update max_honey if the current area is greater than the max_honey.
    Then, I will greedily choose to either increment the left pointer or decrement the right pointer, depending on which pointer has the shorter height.
    I will continue doing this until the left pointer is no longer less than the right pointer.
    Finally, I will return max_honey.

3. Translate each sub-problem into pseudocode:

    Subproblem 1: Calculating the area of the container formed by the two pointers, and updating max_honey accordingly.

        honey <- minimum of height[l] and height[r] * (r - l)
        max_honey <- maximum of max_honey and area

    Subproblem 2: Greedily choosing which pointer to increment or decrement.

        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1

4. Implement the pseudocode in Python:
    def most_honey(height):
        l = 0
        r = len(height) - 1

        max_honey = 0
        while l < r:
            honey = min(height[l], height[r]) * (r - l)
            max_honey = max(max_honey, honey)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return max_honey
"""



