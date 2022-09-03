def alternatingSort(a):
    length = len(a)
    b = []
    for i in range(length):
        if i % 2:
            b.append(a[length - (i // 2) - 1])    # Updated.
        else:
            b.append(a[i // 2])                   # Updated.

    return b