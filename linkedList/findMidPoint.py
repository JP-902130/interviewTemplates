def findMiddle(head):

    # The pointer used to disconnect the left half from the mid node.
    prev = None
    slow = head
    fast = head

    # Iterate until fastPr doesn't reach the end of the linked list.
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Handling the case when slowPtr was equal to head.
    if prev:
        prev.next = None

    return slow

# Function returns 3 for input [1,2,3,4]. The function also separates 1,2 from 3,4. This action makes a lot of questions much simpler
