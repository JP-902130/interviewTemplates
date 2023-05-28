class Union:
    def __init__(self, n):
        self.parent = []
        for i in range(n):
            self.parent.append(i)
        self.weight = [1] * len(self.parent)

    def find(self, node1):
        cur = node1
        while cur != self.parent[cur]:
            cur = self.parent[cur]
        return cur

    def union(self, node1, node2):
        node1Rep = self.find(node1)
        node2Rep = self.find(node2)

        # This means node1 and node2 are already in the same component
        if node1Rep == node2Rep:
            return False
        else:
            if self.weight[node1Rep] > self.weight[node2Rep]:
                # if node1 is bigger, merge node2 to node1
                self.parent[node2Rep] = node1Rep
                self.weight[node1Rep] += self.weight[node2Rep]
            else:
                self.parent[node1Rep] = node2Rep
                self.weight[node2Rep] += self.weight[node1Rep]
        return True
