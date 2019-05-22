class Point(object):

    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        
        return str(self)

    def __str__(self):
        
        return '(%.3f, %.3f, %.3f)' % (self.x, self.y, self.z)



if __name__ == '__main__':

    p1 = Point(1, 2, 3)
    p2 = Point(1, 2, 3)
    p3 = Point(10, 20, 30)

    print('p1: ', p1)
    print('p2: ', p2)
    print('p3: ', p3)

    print('-' * 30)

    print('p1 == p2' if p1 == p2 else 'p1 != p2')
    print('p1 == p3' if p1 == p3 else 'p1 != p3')


