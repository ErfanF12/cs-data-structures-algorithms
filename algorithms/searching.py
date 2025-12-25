def linear_search(arr, target):
    """
    Searches for target in arr using linear search.
    Returns index if found, otherwise returns -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


def binary_search(arr, target):
    """
    Searches for target in a sorted array using binary search.
    Returns index if found, otherwise returns -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
