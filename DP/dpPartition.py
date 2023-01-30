s = ""
cache = {}


def dfs(i):

    if i > len(s) - 1:
        return True
    if i in cache:
        return cache[i]

    # Be aware of the range here
    for j in range(i+1, len(s)+1):
        first = s[i:j]
        if first in wordDict and dfs(j):
            cache[i] = True
            return True
    cache[i] = False
    return False


print(dfs(0))
