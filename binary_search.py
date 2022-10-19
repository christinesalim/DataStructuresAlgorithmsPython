# binary_search.py
# Implements the binary search algorithm. It divides a sorted list
# in half and checks if the key to find is in the middle, lower half or upper
# half of the list.
# Run time: O(logn) because by dividing the list in half each time the number
# of items to search is reduced by half.

def binary_search(arr, start, end, key):
    '''

    :param arr: Sorted list to search
    :param start: starting index of array
    :param end: ending index of array
    :param key: element to search
    :return: index of element if found; -1 if element not found
    '''
    # Need to let start be less than or equal to end to accommodate a list of 1 element
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1  # key is in lower half
        else:
            end = mid - 1  # key is in upper half
    return -1  # key not found


arr = [4, 6, 9, 13, 14, 18, 21, 24]
x = 4
result = binary_search(arr, 0, len(arr) - 1, x)
print(result)
