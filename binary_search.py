def binary_search(array, item):

    """
    The input array is premised as a sorted array in ascending order
    https://en.wikipedia.org/wiki/Binary_search_algorithm
    """

    left  = 0
    right = len(array)

    while left < right:

        mid = int((left + right) / 2)
        mid_item = array[mid]

        if item == mid_item:

            return mid
        
        elif item > mid_item:

            left = mid + 1
        
        else:

            right = mid - 1

    # not found
    return -1        


if __name__ == '__main__':


    arr = list(range(100))

    index = binary_search(arr, 50)

    print('The index of 50 is %d' % index)