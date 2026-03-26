def Selection_Sort(arr):
    arr = [48, 26, 18, 79, 36, 10, 27]
    
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    print("Sorted array:", arr)
    return arr

Selection_Sort([48, 26, 18, 79, 36, 10, 27])''