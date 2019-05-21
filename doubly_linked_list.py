class DoublyLinkedList(object):

    """
    A linked data structure that consists of a set of sequentially linked records called nodes.
    https://en.wikipedia.org/wiki/Doubly_linked_list
    """

    def __init__(self):

        self.head = None
        self.tail = None
    
    def insert(self, item):

        node = Node(item)

        if not self.head:

            self.head = self.tail = node

        else:

            node.prev = self.tail
            node.next = None
            self.tail.next = node 
            self.tail = node
    
    def search(self, item):
        
        # O(n)

        node = self.head

        while node:

            if node.item == item:

                return node
            
            node = node.next

    def remove(self, item):
        
        # O(n)

        node = self.head

        while node:

            if node.item == item:

                if node.prev:
                    
                    # if the current node is node the first element

                    node.prev.next = node.next

                else:

                    # if the current node is the first element
                    self.head = node.next

                if node.next:
                    node.next.prev = node.prev
            
            node = node.next
    
    def show(self):

        node = self.head

        while node:

            item = node.item if node.item else 'nil'
            prev = node.prev.item if node.prev and node.prev.item else 'nil'
            next = node.next.item if node.next and node.next.item else 'nil'
    
            print('prev: %s, current: %s, next: %s' % (prev, item, next))
                
            node = node.next


class Node(object):

    def __init__(self, item):

        self.item = item
        self.prev = None
        self.next = None


if __name__ == '__main__':

    double_list = DoublyLinkedList()

    for i in range(10):
        double_list.insert(i)
        print('inserted: %d' % i)
    
    print('-'*30)

    for i in [0, 3, 5, 9]:
        double_list.remove(i)
        print('removed: %d' % i)

    print('-'*30)

    print('searched: %d' % double_list.search(2).item)

    print('-'*30)

    double_list.show()
    