def find_smallest_index(arr):

    smallest = arr[0]  # store smallest value
    smallest_index = 0  #store index of smallest value

    # print(f"length of array: {len(arr)}")

    for i in range(1, len(arr)):
        #print(f"Index: {i}")
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
            #print(f"new smallest: {arr[i]}")
            #print(f"new smallest index: {i}")
    return smallest_index



def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        print(f"original array: {arr}")
        smallest_index = find_smallest_index(arr) # find smallest index
        new_arr.append(arr.pop(smallest_index))  # remove item with smallest index and add it to new array
        print(f"new array: {new_arr}")
    return new_arr

my_array = [5,4,3,2,1]
print(selection_sort(my_array))

