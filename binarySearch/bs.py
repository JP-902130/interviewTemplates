'''
l is the lower bound of the searching space
r is the upper bound of the searching space
We know that in the searching space:
[l, k-1] does not satisfy the condition, [k, r] satisfy the condition
The following algorithm will return k, we just need to define our condition
'''
l = 0
r = len(nums) - 1


def bs():

    def condition(mid):
        pass

    while l < r:
        mid = (l + r) // 2
        if condition(mid):
            r = mid
        else:
            l = mid + 1
    return l
