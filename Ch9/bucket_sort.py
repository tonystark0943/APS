def bucket_sort(arr):
    if not arr:
        return arr

    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be integers or floats")

    min_val, max_val = min(arr), max(arr)
    bucket_count = len(arr)

    if min_val == max_val:
        return arr

    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int(((num - min_val) / (max_val - min_val)) * (bucket_count - 1))
        buckets[index].append(num)

    result = []
    for b in buckets:
        result.extend(sorted(b))

    return result


print(bucket_sort([0.42, 0.32, 0.23, 0.52, 0.25, 0.47]))  
print(bucket_sort([42, 32, 23, 52, 25, 47]))              
print(bucket_sort([5, 3.2, 7.7, 1, 4.5]))