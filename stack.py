class Stack(object):

    """
    LIFO: Last in First Out
    https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """

    def __init__(self):

        self.items = []

    def push(self, item):

        self.items.append(item)
    
    def pop(self):

        if len(self.items) == 0:
            
            raise ValueError('No item is stacked.')

        return self.items.pop()
    
    @property
    def has_item(self):

        return len(self.items) > 0


if __name__ == '__main__':

    stack = Stack()

    for i in range(10):
        stack.push(i)
        print('pushed: %d' % i)
    
    print('-'*30)

    while stack.has_item:

        i = stack.pop()
        print('popped: %d' % i)

    