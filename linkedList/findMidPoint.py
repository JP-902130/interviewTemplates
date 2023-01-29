class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


head = Node()

slow = head
fast = head.next
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

endOfFirstHalf = slow
