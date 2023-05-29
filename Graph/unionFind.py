class Union:
    def __init__(self, n):
        self.parent = []
        self.weight = []
        self.count = 0
        for i in range(n):
            self.parent.append(-1)
            self.weight.append(0)

    def find(self, node1):
        if node1 == self.parent[node1]:
            return node1
        else:
            return self.find(self.parent[node1])

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

    def isDeveloped(self, node):
        return self.parent[node] != -1

    def develop(self, node):
        if self.isDeveloped(node):
            return
        else:
            self.count += 1
            self.parent[node] = node
            self.weight[node] = 1
