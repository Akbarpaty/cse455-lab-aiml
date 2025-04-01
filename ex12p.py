def abp(n, d, a, b, mx, lst, h):
    if d == h:  
        return lst[n]

    if mx:
        v = float('-inf')
        for i in range(2):  
            v = max(v, abp(n * 2 + i, d + 1, a, b, False, lst, h))
            a = max(a, v)
            if b <= a:
                break
        return v
    else:
        v = float('inf')
        for i in range(2):  
            v = min(v, abp(n * 2 + i, d + 1, a, b, True, lst, h))
            b = min(b, v)
            if b <= a:
                break
        return v


lst = [3, 5, 6, 9, 1, 2, 0, -1]  
h = 3 

print("Best Val:", abp(0, 0, float('-inf'), float('inf'), True, lst, h))
