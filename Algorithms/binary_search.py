def binary_search(target_list, target_item):
    # start with low at 0, since it's the first position of the array
    low = 0
    print(f"low value: {low}")

    # high starts at full list length -1, since array indexes start at 0
    high = len(target_list) - 1
    print(f"high value: {high}")

    times = 0
    # while low is lower or equals to high, iterate until only 1 element is returned
    while low <= high:

        times+=1
        print(f"iteration #: {times}")
        # mid is the sum of low + high, divided (rounded) by 2
        mid = (low + high) // 2
        print(f"mid value (index): {mid}")

        # guess is target list at mid position
        guess = target_list[mid]
        print(f"guess value: {guess}")

        # if item was found, return the position/index (mid)
        if guess == target_item:
            print(f"Found item!, returning index: {mid}")
            return mid

        # if guess was too high, modify high to be mid - 1
        if guess > target_item:
            print(f"Guess [{guess}] was greater than target item [{target_item}], setting high value to [{mid}-1]")
            high = mid - 1
            print(f"New High value: {high}")

        # if guess was too low, modify low to be mid + 1
        else:
            print(f"Guess [{guess}] was lower than target item [{target_item}], setting low value to [{mid}+1]")
            low = mid + 1
            print(f"New low value: {low}")
    print("item not found, returning None...")
    return None

my_list=[1,3,5,7,9]

binary_search(my_list, 3)
print("====================")
binary_search(my_list, -1)
