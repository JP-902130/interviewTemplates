
arr = []

l = 0
r = 0


def condition():
    pass


window = []
while r <= len(arr) - 1:
    window.append(arr[r])

    while condition() == False:
        window.pop(0)
        l += 1

    max_ = max(max_, len(window))
    # len(window) = r-l+1
    r += 1

return max_
