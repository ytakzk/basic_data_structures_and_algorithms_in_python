"""
Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
O(N^2)
https://en.wikipedia.org/wiki/Insertion_sort
"""

def insertion_sort(array):

    for i in range(1, len(array)):

        value = array[i]

        j = i - 1

        while j >= 0 and array[j] > value:

            array[j + 1] = array[j]
            j -= 1
        
        array[j + 1] = value


if __name__ == '__main__':

    array = []

    for i in [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]:

        array.append(i)

    print(array)

    insertion_sort(array)

    print('-' * 50)
    print(array)