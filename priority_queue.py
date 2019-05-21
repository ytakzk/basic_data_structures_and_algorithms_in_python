from heap import Heap

class PriorityQueue(Heap):

    """
    An abstract data type which is like a regular queue or stack data structure, but where additionally each element has a "priority" associated with it
    https://en.wikipedia.org/wiki/Priority_queue
    """

    def __init__(self, is_max_heap=True):
        
        Heap.__init__(self)

        self.is_max_heap = is_max_heap

    def insert(self, item):

        self.items.append(item)

        i      = len(self.items) - 1
        parent = int((i + 1) / 2) - 1
        while i >= 0 and self.items[parent] < self.items[i]:

            self.items[i], self.items[parent] = self.items[parent], self.items[i]

            i    = int((i + 1) / 2)
            left = int((i + 1) / 2) - 1
    
    def pop(self):

        if self.length < 1:

            return None
        
        item = self.items[0]
        last = self.items.pop()
        
        if self.length > 0:

            self.items[0] = last

            if self.is_max_heap:

                self.max_heapify(0)

            else:

                self.min_heapify(0)

        return item
    
    def __str__(self):

        return ' '.join([str(i) for i in self.items])


if __name__ == '__main__':

    queue = PriorityQueue()

    queue.insert(8)
    queue.insert(2)

    print(queue.pop())

    queue.insert(10)

    print(queue.pop())

    queue.insert(11)

    print(queue.pop())
    print(queue.pop())
