def selection_sort(arr):

    n = len(arr)

    for i in range(n):

        min_index = i

        # Find minimum element
        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        # Swap elements
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [64, 25, 12, 22, 11]

print("Original List:", arr)

selection_sort(arr)

print("Sorted List:", arr)