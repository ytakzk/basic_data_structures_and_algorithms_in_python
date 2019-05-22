from vector import Vector

class Point(Vector):

    def __init__(self, x, y, z):

        Vector.__init__(self, float(x), float(y), float(z))

    def __eq__(self, other):
        
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        
        return str(self)

    def __str__(self):
        
        return '(%.3f, %.3f, %.3f)' % (self.x, self.y, self.z)

    def distance_to(self, point):

        return (self - point).length

    @staticmethod
    def ccw(point0, point1, point2):

        # just consider the points as 2d points (z value is ignored.)

        EPSILON = 0.0000001

        COUNTER_CLOCKWISE = 1
        CLOCKWISE         = 2
        ONLINE_BACK       = 3
        ONLINE_FRONT      = 4
        ON_SEGMENT        = 5

        vec1 = (point1 - point0)
        vec2 = (point2 - point0)

        cross_product = vec1.x * vec2.y - vec1.y * vec2.x
        
        if cross_product > EPSILON:

            return COUNTER_CLOCKWISE
        
        elif cross_product < -EPSILON:

            return CLOCKWISE
        
        dot_product = vec1.x * vec2.x + vec1.y * vec2.y

        if dot_product < -EPSILON:

            return ONLINE_BACK

        norm1 = vec1.x ** 2 + vec1.y ** 2
        norm2 = vec2.x ** 2 + vec2.y ** 2
        
        if norm1 < norm2:

            return ONLINE_FRONT
        
        else:

            return ON_SEGMENT


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

    print('-' * 30)
    print('The distance between p1 and p3 is', p1.distance_to(p3))

    print('-' * 30)

    p4  = Point(0, 0, 0)
    p5  = Point(10, 0, 0)
    p6  = Point(10, 10, 0)
    p7  = Point(10, -10, 0)
    p8  = Point(-5, 0, 0)
    p9  = Point(15, 0, 0)
    p10 = Point(5, 0, 0)

    print(Point.ccw(p4, p5, p6))
    print(Point.ccw(p4, p5, p7))
    print(Point.ccw(p4, p5, p8))
    print(Point.ccw(p4, p5, p9))
    print(Point.ccw(p4, p5, p10))
