### WEEK 5, SESSION 2, Advanced Problem Set Version 1

# QUESTION 1: Greatest Node

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should the function handle empty linked lists (None head) gracefully?
    Q2: What should be returned if the linked list contains only negative numbers?

2. Write out in plain English what you want to do:

    I need to traverse the entire linked list starting from the head node,
    keeping track of the maximum value encountered. I'll initialize a maximum
    value variable to negative infinity, then iterate through each node,
    updating the maximum when I find a larger value. After visiting all nodes,
    I'll return the maximum value found.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Initialize traversal variables
    max_val <- negative infinity
    curr <- head
    
    Subproblem 2: Traverse and find maximum
    while curr is not None:
        max_val <- maximum of max_val and curr.value
        curr <- curr.next
    
    Subproblem 3: Return result
    return None if max_val equals negative infinity else max_val

4. Translate the pseudocode into Python and share your final answer:
    def find_max(head):
        max_val = float("-inf")
        curr = head
        while curr: 
            max_val = max(max_val, curr.value)
            curr = curr.next
        return None if max_val == float("-inf") else max_val

Time Complexity: O(n) where n is the number of nodes in the linked list, as we visit each node exactly once.
Space Complexity: O(1) as we only use a constant amount of extra space for variables max_val and curr.

"""

# QUESTION 2: Remove Tail

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: What should happen when the linked list has only one node?
    Q2: Should the function modify the original list or create a new one?

2. Write out in plain English what you want to do:

    I need to remove the last node from a linked list. The key insight is that
    I need to find the second-to-last node and set its next pointer to None.
    I'll handle edge cases for empty lists and single-node lists first, then
    traverse to find the node whose next.next is None, and update its next pointer.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Handle edge cases
    if head is None: return None
    if head.next is None: return None
    
    Subproblem 2: Find second-to-last node
    current <- head
    while current.next and current.next.next:
        current <- current.next
    
    Subproblem 3: Remove tail
    current.next <- None
    return head

4. Translate the pseudocode into Python and share your final answer:
    def remove_tail(head):
        if head is None:
            return None
        if head.next is None:
            return None 
            
        current = head
        while current.next and current.next.next: 
            current = current.next

        current.next = None 
        return head

Time Complexity: O(n) where n is the number of nodes, as we traverse to the second-to-last node.
Space Complexity: O(1) as we only use a constant amount of extra space for the current pointer.

"""

# QUESTION 3: Delete Duplicates in a Linked List

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should we remove all occurrences of duplicated values or just the extra copies?
    Q2: How should we handle the case where the head node itself is a duplicate?

2. Write out in plain English what you want to do:

    I need to remove all nodes that have duplicate values, not just the extra copies.
    Since the head might be removed, I'll use a temporary head technique. I'll traverse
    the list, and for each value, check if it appears more than once. If it does,
    I'll skip all nodes with that value. If it appears only once, I'll keep it
    in the result list.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Initialize temporary head
    temp_head <- new Node with None value
    curr <- temp_head
    
    Subproblem 2: Process each unique value
    while head is not None:
        curr_val <- head.value
        new_next <- head.next
        duplicate <- False
        
        while new_next and new_next.value equals curr_val:
            new_next <- new_next.next
            duplicate <- True
        
        if not duplicate:
            curr.next <- head
            curr <- curr.next
            head <- new_next
        else:
            curr.next <- new_next
            curr <- curr.next
            head <- new_next
    
    return temp_head.next

4. Translate the pseudocode into Python and share your final answer:
    def delete_dupes(head):
        temp_head = Node(None)
        curr = temp_head
      
        while head:
            curr_val = head.value
            new_next = head.next
            duplicate = False
            while new_next and new_next.value == curr_val:
                new_next = new_next.next
                duplicate = True
            if not duplicate: 
                curr.next = head
                curr = curr.next
                head = new_next
            else: 
                curr.next = new_next
                curr = curr.next
                head = new_next

        return temp_head.next

Time Complexity: O(n) where n is the number of nodes, as we visit each node at most twice.
Space Complexity: O(1) as we only use a constant amount of extra space for pointers.

"""

# QUESTION 4: Does it Cycle?

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: Should we handle the case where the linked list is empty or has only one node?
    Q2: What happens if there are multiple cycles in the linked list?

2. Write out in plain English what you want to do:

    I'll use the Floyd's cycle detection algorithm (tortoise and hare). I'll maintain
    two pointers: a slow pointer that moves one step at a time, and a fast pointer
    that moves two steps at a time. If there's a cycle, the fast pointer will
    eventually catch up to the slow pointer. If there's no cycle, the fast pointer
    will reach the end of the list.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Initialize pointers
    slow <- head
    fast <- head
    
    Subproblem 2: Move pointers and check for cycle
    while fast and fast.next:
        slow <- slow.next
        fast <- fast.next.next
        
        if slow equals fast:
            return True
    
    return False

4. Translate the pseudocode into Python and share your final answer:
    def has_cycle(head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

Time Complexity: O(n) where n is the number of nodes, as in the worst case we visit each node once.
Space Complexity: O(1) as we only use two pointer variables regardless of input size.

"""

# QUESTION 5: Remove Nth Node From End of List

"""

1. Share 2 questions you would ask to help understand the question:

    Q1: What should happen if n is greater than the length of the list?
    Q2: Should we handle the case where n equals the length of the list (removing the head)?

2. Write out in plain English what you want to do:

    I need to remove the nth node from the end of the linked list. First, I'll
    calculate the total length of the list. Then I'll determine which node to
    remove by converting the "nth from end" to "index from beginning". I'll use
    a temporary head technique to handle the case where the head needs to be removed,
    and traverse to the position just before the target node to perform the removal.

3. Translate each sub-problem into pseudocode:
    
    Subproblem 1: Calculate list length
    curr_idx <- 0
    length_list <- 0
    curr <- head
    while curr:
        curr <- curr.next
        length_list <- length_list + 1
    
    Subproblem 2: Find position to remove
    target_index <- length_list - n
    
    Subproblem 3: Use temporary head and traverse to removal position
    temp_head <- new Node with None value
    curr <- temp_head
    temp_head.next <- curr
    
    while curr_idx < target_index:
        curr.next <- head
        head <- head.next
        curr <- curr.next
        curr_idx <- curr_idx + 1
    
    Subproblem 4: Remove target node
    head <- head.next if head exists else None
    curr.next <- head
    
    return temp_head.next

4. Translate the pseudocode into Python and share your final answer:
    def remove_nth_from_end(head, n):
        curr_idx = 0
        length_list = 0
        
        curr = head
        while curr: 
            curr = curr.next
            length_list += 1

        temp_head = Node(None)
        curr = temp_head
        temp_head.next = curr

        while curr_idx < length_list - n:
            curr.next = head
            head = head.next
            curr = curr.next
            curr_idx += 1
        

        head = head.next if head else None
        curr.next = head

        return temp_head.next

Time Complexity: O(n) where n is the number of nodes, as we traverse the list twice (once to count, once to remove).
Space Complexity: O(1) as we only use a constant amount of extra space for pointer variables.

"""