def bubblesort(unsorted_list):

    n = len(unsorted_list)  
    swap = False

    comparisons = 0
    passes = 0
    exchanges = 0

    for i in range(n-1):
        passes += 1
        for j in range(n-i-1):
            comparisons += 1
            if unsorted_list[j] > unsorted_list[j + 1]:
                exchanges += 1
                swap = True
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
                print(unsorted_list)

        if not swap:
            return
        
    return comparisons, exchanges, passes


if __name__ == "__main__": 
    l1 = [23, 17, 45, 6, 78, 21]              
    print(f"comparisons, exchanges, passes: {bubblesort(l1)}")
