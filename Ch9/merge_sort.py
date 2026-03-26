def merge_sort(arr):
    length = len(arr)
    if length == 1 or length == 0:
        return arr
    mid_point = length//2
    left = merge_sort(arr[:mid_point])
    right = merge_sort(arr[mid_point:])
    sorted_arr = merge_lists(left, right)
    return sorted_arr
def merge_lists(L1, L2):
    res = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            res.append(L1[i])
            i += 1
        else:
            res.append(L2[j])
            j += 1
        res += L1[i]
        res += L2[j]
    return res
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr) 