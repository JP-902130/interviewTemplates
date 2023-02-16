class Node:
    def __init__(self, val, next) -> None:
        self.val = val
        self.next = next


head = Node()

# Stop at the last
# cur will be the last element after the iteration
while cur and cur.next:
    cur = cur.next

# Stop at None
# cur will become None after the iteration
while cur:
    cur = cur.next
