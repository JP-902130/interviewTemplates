class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


# This version returns 2 for the list 1 2 3 4
head = Node()
slow = head
fast = head.next
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

endOfFirstHalf = slow

# This version returns 3 for the list 1 2 3 4
head = Node()
slow = head
fast = head
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

endOfFirstHalf = slow

'''
1) Both versions work, but sometimes one works better then the other. 
'''
