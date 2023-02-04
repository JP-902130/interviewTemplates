'''
Pattern:
- Each time we add a new element to the window, we need to make sure that the weight of the window should increase, each time we shrink the window, the weight should decrease.
'''


def dynamic_size():
    arr = []
    l = 0
    r = 0

    def condition():
        pass

    window = []
    max_ = 0
    while r <= len(arr) - 1:
        window.append(arr[r])

        while condition() == False:
            window.pop(0)
            l += 1

        max_ = max(max_, len(window))
        # len(window) = r-l+1
        r += 1

    return max_


def fixed_size(s, windowSize):

    # Window init
    r = 0
    l = 0

    window = []
    res = []
    for i in range(windowSize-1):
        window.append(s[i])
        r = i
    r += 1

    # Window process
    while r <= len(s) - 1:
        window.append(s[r])

        # check the window
        res.append(window.copy())
        window.pop(0)

        r += 1
        l += 1

    return res
