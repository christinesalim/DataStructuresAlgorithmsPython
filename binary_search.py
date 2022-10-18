
# Run time: O(logn)
def binary_search(arr, start, end, key):
    # Need to let start be less than or equal to end to accomodate a list of 1 element
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
