"""
Selection sort finds the minimum or maximum element in an unsorted array and then putting it in its correct position in a sorted array.
O(N^2)
https://en.wikipedia.org/wiki/Selection_sort
"""

def selection_sort(array):

    length = len(array)

    for i in range(length):

        min_j = i

        for j in range(i + 1, length):

            if array[j] < array[min_j]:

                min_j = j

        array[i], array[min_j] = array[min_j], array[i]


if __name__ == '__main__':

    array = []

    for i in [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]:

        array.append(i)

    print(array)

    selection_sort(array)

    print('-' * 50)
    print(array)