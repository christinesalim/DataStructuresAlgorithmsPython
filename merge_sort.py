# merge_sort.py
# Implements the merge sort algorithm to sort a list by using the
# divide and conquer strategy. The list to be sorted is divided in
# half each time until a list of 1 element is made. Then the smaller
# lists are combined together and sorted at each level until the full
# list is sorted.
# Run-time O(nlogn) There are log(n) operations to divide the list in
# half each time and n operations to merge the list together

def merge_sort(unsorted_list):
    """
    Recursively divide the list in half and call this function on
    each half to sort the list
    :param unsorted_list:
    :return: sorted list
    """

    # Base case: return the same list when it only has 1 element
    if len(unsorted_list) == 1:
        return unsorted_list

    mid = len(unsorted_list)//2
    print("mid:", mid)
    # Recursively call merge_sort on each half of the list
    sorted_first_half = merge_sort(unsorted_list[:mid])
    sorted_second_half = merge_sort(unsorted_list[mid:])

    return merge(sorted_first_half, sorted_second_half)


def merge(first_half, second_half):
    """
    Merges two lists by comparing elements in both lists and sorting them in
    order
    :param first_half:
    :param second_half:
    :return: sorted list
    """
    i = j = 0
    merged_list = []
    while i < len(first_half) and j < len(second_half):
        if first_half[i] <= second_half[j]:
            merged_list.append(first_half[i])
            i += 1
        else:
            merged_list.append(second_half[j])
            j += 1
    # check if any more elements are left in first_half
    while i < len(first_half):
        merged_list.append(first_half[i])
        i += 1

    # check if any more elements are left in second_half
    while j < len(second_half):
        merged_list.append(second_half[j])
        j += 1

    return merged_list


list1 = [11, 12, 7, 41, 61, 13, 16, 14]
print("Unsorted list", list1)

print(merge_sort(list1))
