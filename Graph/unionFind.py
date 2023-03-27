parent = []
'''
The parentent array is working the same way as the one in "Finding the duplicate number"
For any index i in parent, parent[i] refers to the node that i points to.
Originally, every node points at itself.
If a node points at itself, then the node is called the root node, also called the representitive of the graph component
'''
rank = []
for i in range(n):
    parent.append(i)
    rank.append(1)


def findRoot(n1):
    cur = n1
    while cur != parent[cur]:
        cur = parent[cur]
    return cur


def union(n1, n2):
    root1, root2 = findRoot(n1), findRoot(n2)
    if root1 == root2:
        return 0

    elif rank[root2] > rank[root1]:
        parent[root1] = parent[root2]
        rank[root2] += rank[root1]
    else:
        parent[root2] = parent[root1]
        rank[root1] += rank[root2]
    return 1
