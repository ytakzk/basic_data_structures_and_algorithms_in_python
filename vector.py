import math
from point import Point

class Vector(Point):
    
    def __init__(self, x, y, z):

        Point.__init__(self, float(x), float(y), float(z))

    def __add__(self, other):

        vec = Vector(self.x, self.y, self.z)
        return vec.add(other)

    def __sub__(self, other):

        vec = Vector(self.x, self.y, self.z)
        return vec.subtract(other)

    def __mul__(self, other):

        # scale
        if (type(other) is int or type(other) is float):

            vec = Vector(self.x, self.y, self.z)
            return vec.scale(other)

        # dot_product
        elif isinstance(other, Vector):

            return (
                self.x * other.x +
                self.y * other.y +
                self.z * other.z
            )

        else:

            raise ValueError(type(other) + ' is an invalid input for multiplying')

    # for python 3
    def __truediv__(self, other):

        if (type(other) is int or type(other) is float):

            vec = Vector(self.x, self.y, self.z)
            return vec.divide(other)

        elif isinstance(other, Vector):

            return Vector(self.x / other.x, self.y / other.y, self.z / other.z)

        else:

            raise ValueError(type(other) + ' is an invalid input for dividing')

    # for python 2
    def __div__(self, other):

        if (type(other) is int or type(other) is float):

            vec = Vector(self.x, self.y, self.z)
            return vec.divide(other)

        elif isinstance(other, Vector):

            return Vector(self.x / other.x, self.y / other.y, self.z / other.z)

        else:

            raise ValueError(type(other) + ' is an invalid input for dividing')


    def __matmul__(self, other):

        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def add(self, other):

        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def subtract(self, other):

        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def scale(self, factor):

        self.x *= factor
        self.y *= factor
        self.z *= factor
        return self

    def divide(self, factor):

        self.x /= factor
        self.y /= factor
        self.z /= factor
        return self

    @property
    def length(self):

        return math.sqrt(self.x ** 2 +self.y ** 2 + self.z ** 2)

    @property
    def unitize(self):

        l = self.length

        if l == 0:

            return self

        return self.divide(l)

    def cross_product(self, other):

        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def is_orthogonal_to(self, other):

        return self * other == 0

    def is_parallel_to(self, other):

        normal = self.cross_product(other)
        return normal.x == 0 and normal.y == 0 and normal.z == 0


if __name__ == '__main__':

    v1 = Vector(10, 20, 30)
    v2 = Vector(1, 2, 3)
    v3 = Vector(1, 2, 3)
    v4 = Vector(1, 0, 0)
    v5 = Vector(0, 1, 0)

    print('v1: ', v1)
    print('v2: ', v2)
    print('v3: ', v3)
    print('v4: ', v4)
    print('v5: ', v5)

    print('-' * 30)

    print('v1 == v2' if v1 == v2 else 'v1 != v2')
    print('v2 == v3' if v2 == v3 else 'v2 != v3')

    print('-' * 30)

    print('v1 + v3 =', v1 + v3)
    print('v1 - v3 =', v1 - v3)
    print('v1 *  2 =', v1 * 2)
    print('v1 / v3 =', v1 / v3)

    print('-' * 30)
    print('dot product of v1 and v3: ', v1 * v3)
    print('cross product of v4 and v5: ', v4.cross_product(v5))

    print('-' * 30)
    print('length of v1: : ', v1.length)
    print('unit vector of v1: ', v1.unitize)

    print('-' * 30)
    print('v4 is orthogonal to v5' if v4.is_orthogonal_to(v5) else 'v4 is not orthogonal to v5')
    print('v2 is parallel to v3' if v2.is_parallel_to(v3) else 'v2 is not parallel to v3')
