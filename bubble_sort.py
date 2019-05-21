"""
A simple sorting algorithm that repeatedly steps through the list, compares adjacent pairs and swaps them if they are in the wrong order.
O(N^2)
https://en.wikipedia.org/wiki/Bubble_sort
"""

def bubble_sort(array):

    num = len(array)
 
    for i in range(num):
 
        for j in range(0, num - i - 1):

            next_j = j + 1
 
            if array[j] > array[next_j]:

                array[j], array[next_j] = array[next_j], array[j]


if __name__ == '__main__':

    array = []

    for i in [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]:

        array.append(i)

    print(array)

    bubble_sort(array)

    print('-' * 50)
    print(array)