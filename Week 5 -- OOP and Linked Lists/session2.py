### WEEK 5, SESSION 2, Advanced Problem Set Version 1

# Problem 1: Greatest Node

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def find_max(head):
#     max_val = float("-inf")
#     curr = head
#     while curr: 
#         max_val = max(max_val, curr.value)
#         curr = curr.next
#     return None if max_val == float("-inf") else max_val







# Problem 2: Remove Tail
# class Node:
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next
        
# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def remove_tail(head):
#     if head is None:
#         return None
#     if head.next is None:
#         return None 
        
#     current = head
#     while current.next and current.next.next: 
#         current = current.next

#     current.next = None 
#     return head

# head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# # Linked List: Isabelle -> Alfonso -> Cyd
# print_linked_list(remove_tail(head))










# Problem 3: Delete Duplicates in a Linked List

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def delete_dupes(head):
#     temp_head = Node(None)
#     curr = temp_head
  
#     while head:
#         curr_val = head.value
#         new_next = head.next
#         duplicate = False
#         while new_next and new_next.value == curr_val:
#             new_next = new_next.next
#             duplicate = True
#         if not duplicate: 
#             curr.next = head
#             curr = curr.next
#             head = new_next
#         else: 
#             curr.next = new_next
#             curr = curr.next
#             head = new_next

#     return temp_head.next









# Problem 4: Does it Cycle?

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def has_cycle(head):
#     slow = head
#     fast = head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next

#         if slow == fast:
#             return True
#     return False







# Problem 5: Remove Nth Node From End of List

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def remove_nth_from_end(head, n):
#     curr_idx = 0
#     length_list = 0
    
#     curr = head
#     while curr: 
#         curr = curr.next
#         length_list += 1

#     temp_head = Node(None)
#     curr = temp_head
#     temp_head.next = curr

#     while curr_idx < length_list - n:
#         curr.next = head
#         head = head.next
#         curr = curr.next
#         curr_idx += 1
    

#     head = head.next if head else None
#     curr.next = head

#     return temp_head.next
