class Heap(object):

    """
    A specialized tree-based data structure which is essentially an almost complete tree that satisfies the heap property.
    https://en.wikipedia.org/wiki/Heap_(data_structure)
    """
    def __init__(self):

        self.items = []
    
    def append(self, item):

        self.items.append(item)
    
    def get(self, i):

        return self.items[i]

    @property
    def length(self):

        return len(self.items)    

    def max_heapify(self, i):

        i += 1 # 0-origin to 1-origin

        left  = 2 * i
        right = left + 1

        # 1-origin to 0-origin
        left  -= 1
        right -= 1
        i     -= 1

        num = len(self.items)

        if left < num and self.items[left] > self.items[i]:

            largest = left

        else:

            largest = i

        if right < num and self.items[right] > self.items[largest]:

            largest = right

        if largest != i:
            
            self.items[i], self.items[largest] = self.items[largest], self.items[i]
            self.max_heapify(largest)

    def min_heapify(self, i):

        i += 1 # 0-origin to 1-origin

        left  = 2 * i
        right = left + 1

        # 1-origin to 0-origin
        left  -= 1
        right -= 1
        i     -= 1

        num = len(self.items)

        if left < num and self.items[left] < self.items[i]:

            largest = left

        else:

            largest = i

        if right < num and self.items[right] < self.items[largest]:

            largest = right

        if largest != i:
            
            self.items[i], self.items[largest] = self.items[largest], self.items[i]
            self.min_heapify(largest)

    def sort(self, max_heaptify=True):
        
        for i in range(int(self.length / 2), -1, -1):

            if max_heaptify:
            
                self.max_heapify(i)

            else:

                self.min_heapify(i)

if __name__ == '__main__':

    heap = Heap()

    for item in [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]:

        heap.append(item)

    heap.sort()

    for i in range(heap.length):

        print(heap.get(i))