def solution(n, a):
    b = []
    if n == 1:
        return a
        
    for i in range(n):
        if i == 0:
            item = a[i] + a[i+1]
            b.append(item)
        elif i == n-1:
            item = a[i-1] + a[i]
            b.append(item)
        else:
            item = a[i-1] + a[i] + a[i+1]
            b.append(item)
    return b