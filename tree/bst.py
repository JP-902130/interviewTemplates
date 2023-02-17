class Node:
    def __init__(self, val, left, right):
        return


def leftBigAndRightSmall(node):
    cur = node.left
    while cur and cur.right:
        cur = cur.right
    leftBig = cur.val

    cur = node.right
    while cur and cur.left:
        cur = cur.left
    rightSmall = cur.val
