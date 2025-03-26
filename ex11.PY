import math

def fun(x, y, z, lst, h, path):
    path.append(y)

    if x == h:
        return lst[y], path

    if z:
        left_val, left_path = fun(x + 1, y * 2, False, lst, h, path[:])
        right_val, right_path = fun(x + 1, y * 2 + 1, False, lst, h, path[:])

        if left_val > right_val:
            return left_val, left_path
        else:
            return right_val, right_path
    else:
        left_val, left_path = fun(x + 1, y * 2, True, lst, h, path[:])
        right_val, right_path = fun(x + 1, y * 2 + 1, True, lst, h, path[:])

        if left_val < right_val:
            return left_val, left_path
        else:
            return right_val, right_path

def finding(n):
    return math.log2(n)

num_list = [3, 5, 2, 9, 12, 5, 23, 23]  
tree_size = int(finding(len(num_list)))

answer, path_taken = fun(0, 0, True, num_list, tree_size, [])

print("element", answer)
print("path is ", path_taken)
