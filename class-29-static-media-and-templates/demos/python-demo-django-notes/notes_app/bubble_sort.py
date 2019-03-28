def bubble_sort(arr):
    """
    sorts given array in place
    using bubble sort algo
    (returning for convenience)
    """

    end_index = len(arr) - 1

    while(end_index > 1):

        for i in range(end_index):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        end_index -= 1

    return arr

print(bubble_sort([7,5,3,8,6]))