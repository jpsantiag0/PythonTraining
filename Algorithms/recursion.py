def countdown(i):
    print(i)
    if i<=1:  # base case
        return
    else:
        countdown(i-1)  # recursive case

#countdown(10)


# Factorial:
# 3! = 3 * 2 * 1  -> 6
# 5! = 5 * 4 * 3 * 2 * 1 -> 120
def factorial(x):
    print(f"x value: {x}")
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))


def sum_array(arr):
    total = 0
    for item in arr:
        total += item
    return total

print("Sum up elements in list using recursion")
def sum_array_recursion(arr):
    if len(arr) == 0:
        return 0
    #elif len(arr) == 1:
    #    return arr[0]
    else:
        #first_element = arr[0]
        #arr.pop(0)
        #return first_element + sum_array_recursion(arr)
        return arr[0] + sum_array_recursion(arr[1:])

print(sum_array_recursion([1,2,3,1]))

print("*********************************")

print("Count Items in list using recursion")
def count_items_recursion(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + count_items_recursion(arr[1:])
print(count_items_recursion([1,2,3,1, 2]))

print("*********************************")

print("Find Maximum number in a list")
def find_max_item(arr):
    print(f"Array[0] = {arr[0]}")
    if len(arr) == 1:
        return arr[0]
    else:
        max_of_rest = find_max_item(arr[1:])
        print(f"Max of Rest = {max_of_rest}")
        return arr[0] if arr[0] > max_of_rest else max_of_rest

print(find_max_item([1,5,3,4]))

print("Binary Search")
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        guess = arr[mid]

        if guess == item:
            print(f"Found item!")
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None





my_arr = [1,2,3,4]
print(binary_search(my_arr, 3))


print(f"Binary search recursion")
def binary_search_recursion(arr, item, low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    guess = arr[mid]

    if guess == item:
        return mid

    elif guess > item:
        return binary_search_recursion(arr, item, low, mid - 1)
    else:
        return binary_search_recursion(arr, item, mid + 1, high)

print(binary_search_recursion(my_arr, 3, 0, len(my_arr) -1 ))