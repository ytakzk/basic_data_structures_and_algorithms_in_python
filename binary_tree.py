class BinaryTree(object):

    """
    A tree data structure in which each node has at most two children
    https://en.wikipedia.org/wiki/Binary_tree
    """

    def __init__(self):

        self.root = None

    def insert(self, item):

        # O(n)

        new_node = Node(item)

        # get the parent of the new node
        node   = self.root
        parent = None

        while node:
            
            parent = node

            if new_node.item < node.item:

                node = node.left
            
            elif new_node.item > node.item:

                node = node.right

            else:
                
                raise ValueError('Cannot contain the same value')
        
        new_node.parent = parent

        # assign the new node as a children of its parent
        if not parent:

            self.root = new_node
        
        elif new_node.item < parent.item:

            parent.left = new_node

        else:

            parent.right = new_node
    
    def delete(self, item):

        node = self.search(item)
        
        if self.root == node:
            
            parent = self.root

        else:
            
            parent = node.parent

        if not node.left and not node.right:

            # has no children
            # remove the node from its tree.

            if node.item < parent.item:

                parent.left = None
                
            else:
                
                parent.right = None
    
        elif node.left and not node.right:

            # has a single child in its left
            # remove the node from its tree.

            if node.item < parent.item:

                parent.left = node.left

            else:
                
                parent.right = node.left
            
            node.left.parent = parent

        elif not node.left and node.right:

    		# has a single child in its right
            # remove the node from its tree

            if node.item < parent.item:

                parent.left = node.right

            else:
                
                parent.right = node.right
        
            node.right.parent = parent

        else:

            # has two children
            # remove the min node from its tree and assign its value to the node to be deleted.
            # the node is not deleted from the tree.
            min_node  = node.minimum
            node.item = min_node.item
            min_node.parent.left = None

        
    def search(self, item):

        node = self.root

        while node and node.item != item:

            node = node.left if item < node.item else node.right

        return node

    def inorder(self, node):

        if not node:

            return
        
        self.inorder(node.left)
        print(node.item)
        self.inorder(node.right)

    def preorder(self, node):

        if not node:

            return
        
        print(node.item)
        self.preorder(node.left)
        self.preorder(node.right)
    
    def depth_of(self, item):

        depth = 0
        
        node = self.root

        while node and node.item != item:

            node = node.left if item < node.item else node.right
            depth += 1

        return depth if node else -1



class Node(object):

    def __init__(self, item):

        self.item   = item
        self.parent = None
        self.left   = None
        self.right  = None

    @property
    def minimum(self):

        node = self
        while node.left:

            node = node.left

        return node

if __name__ == '__main__':

    binary_tree = BinaryTree()

    binary_tree.insert(8)
    binary_tree.insert(2)
    binary_tree.insert(3)
    binary_tree.insert(7)
    binary_tree.insert(22)
    binary_tree.insert(1)

    print(binary_tree.search(1))
    print(binary_tree.search(2))
    print(binary_tree.search(3))
    print(binary_tree.search(4))
    print(binary_tree.search(5))
    print(binary_tree.search(6))
    print(binary_tree.search(7))
    print(binary_tree.search(8))

    print('-' * 50)

    print('inorder')
    binary_tree.inorder(binary_tree.root)
    
    print('-' * 50)

    print('preorder')
    binary_tree.preorder(binary_tree.root)

    print('-' * 50)

    binary_tree.delete(3)
    binary_tree.delete(7)

    print('-' * 50)

    print('inorder')
    binary_tree.inorder(binary_tree.root)
    
    print('-' * 50)

    print('preorder')
    binary_tree.preorder(binary_tree.root)

