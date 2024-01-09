def binarySearch(item_list, lower, upper, target): 

    while lower <= upper:
        mid = (lower + upper) // 2

        if item_list[mid] > target:
            upper = mid - 1
        elif item_list[mid] < target:
            lower = mid + 1

        else:
            return f"Item found at position {mid}"
    return "Item not in list"


def recursiveBinary(item_list, lower, upper, target): 

    if upper >= lower:
        mid = (lower + upper) // 2

        if item_list[mid] == target:
            return f"Item found at position {mid}"

        if item_list[mid] > target:
            return recursiveBinary(item_list, lower, mid - 1, target)
        elif item_list[mid] < target:
            return recursiveBinary(item_list, mid + 1, upper, target)

    else:
        return f"Item not in list"


if __name__ == "__main__":

    l1 = [0, 1, 2, 3, 4, 5, 6]
    print(recursiveBinary(l1, 0, len(l1) - 1, 1))
        

