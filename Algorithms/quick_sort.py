def quicksort(arr):
    if len(arr) < 2: # Base case, arrays with 0 and 1 elements are already "sorted"
        return arr
    else: # Recursive Case
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]  # Sub-array with all elements smaller than pivot
        greater = [i for i in arr[1:] if i > pivot] # Sub-array with all elements greater than pivot
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,5,2,3]))