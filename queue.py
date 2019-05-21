class Queue(object):

    """
    FIFO: First in First Out
    https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
    """

    def __init__(self):

        self.items = []

    def enqueue(self, item):

        self.items.append(item)
    
    def dequeue(self):

        if len(self.items) == 0:
            
            raise ValueError('No item is queued.')

        item = self.items[0]
        self.items = self.items[1:]
        return item
    
    @property
    def is_empty(self):

        return len(self.items) == 0


if __name__ == '__main__':

    queue = Queue()

    for i in range(10):
        queue.enqueue(i)
        print('enqueued: %d' % i)
    
    print('-'*30)

    while not queue.is_empty:

        i = queue.dequeue()
        print('dequeued: %d' % i)

    