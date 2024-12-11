def binary_search(target_list, item):
    low = 0
    high = len(target_list) - 1

    while low<=high:
        mid = (high+low) // 2

        guess = target_list[mid]

        if guess == item:
            print(f"found it!")
            print(mid)
            return mid
        if guess > item:
            # too high
            high = mid - 1
        if guess < item:
            # too low
            low = mid + 1
    print("not found")
    return None

my_list = [1,2,3,4,5,6]
print(binary_search(my_list, 3))


def get_smallest_index(target_list):
    smallest_index = 0
    smallest_item = target_list[0]

    for index in range(1, len(target_list)):
        if target_list[index] < smallest_item:
            smallest_item = target_list[index]
            smallest_index = index

    return smallest_index

def selection_sort(target_list):
    new_arr = []
    for i in range(len(target_list)):
        smallest_index = get_smallest_index(target_list)
        new_arr.append(target_list.pop(smallest_index))

    return new_arr

my_unsorted_list = [8,9,7,5,6,4,3,2,1, 10]
print(selection_sort(my_unsorted_list))
