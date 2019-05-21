class CompleteBinaryTree(object):

    """
    A binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
    https://www.sciencedirect.com/topics/computer-science/complete-binary-tree
    """

    def __init__(self):

        self.items = []
    
    def append(self, item):

        self.items.append(item)

    def parent(self, i):
        
        return int(i / 2)

    def left(self, i):

        return 2 * i
    
    def right(self, i):

        return 2 * i + 1


if __name__ == '__main__':

    tree = CompleteBinaryTree()

    tree.append(7)
    tree.append(8)
    tree.append(1)
    tree.append(2)
    tree.append(3)
    
    for i in range(5):

        item = tree.items[i]

        ii = i + 1 # 0-origin to 1-origin

        parent_key = tree.parent(ii) - 1 # 1-origin to 0-origin
        left_key   = tree.left(ii) - 1   # 1-origin to 0-origin
        right_key  = tree.right(ii) - 1  # 1-origin to 0-origin

        parent = tree.items[parent_key] if parent_key < len(tree.items) else -1
        left   = tree.items[left_key] if left_key < len(tree.items) else -1
        right  = tree.items[right_key] if right_key < len(tree.items) else -1

        print('%d => item: %d, parent: %d, left: %d, right: %d' % (i, item, parent, left, right))

    