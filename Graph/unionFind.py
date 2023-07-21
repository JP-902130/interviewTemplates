# Init all n nodes at the beginning, works the most of the time, simple union find
class Union:
    def __init__(self, n):
        self.parent = []
        self.weight = []
        self.countComp = n
        for i in range(n):
            self.parent.append(i)
            self.weight.append(1)

    def find(self, node):
        cur = node
        while self.parent[cur] != cur:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, node1, node2):
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        if rep1 == rep2:
            return False
        else:
            if self.weight[rep1] > self.weight[rep2]:
                self.parent[rep2] = rep1
                self.weight[rep1] += self.weight[rep2]
            else:
                self.parent[rep2] = rep1
                self.weight[rep1] += self.weight[rep2]
            self.countComp -= 1
            return True

# Init the nodes real-time, also map the matrix to the nodes


class Union:
    def __init__(self, m, n):
        self.parent = []
        self.weight = []
        self.m = m
        self.n = n
        self.count = 0
        for r in range(m):
            for c in range(n):
                self.parent.append(-1)
                self.weight.append(0)

    def find(self, node):
        if self.parent[node] == node:
            return node
        else:
            return self.find(self.parent[node])

    def union(self, node1, node2):
        rep1 = self.find(node1)
        rep2 = self.find(node2)

        if rep1 == rep2:
            return False
        else:
            if self.weight[rep1] > self.weight[rep2]:
                self.parent[rep2] = rep1
                self.weight[rep1] += self.weight[rep2]
            else:
                self.parent[rep2] = rep1
                self.weight[rep1] += self.weight[rep2]
            self.count -= 1
            return True

    def getNode(self, r, c):
        return r * self.n + c

    def getPos(self, node):
        return (node // self.m, node % self.m)

    def isDeveloped(self, node):
        if self.parent[node] >= 0:
            return True
        else:
            return False

    def develop(self, node):
        if self.isDeveloped(node) == True:
            return
        self.parent[node] = node
        self.weight[node] = 1
        self.count += 1
