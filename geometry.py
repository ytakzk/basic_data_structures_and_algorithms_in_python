class Line(object):

    def __init__(self, start, end):

        self.start = start
        self.end   = end


class Circle(object):

    def __init__(self, center, radius, normal):

        self.center = center
        self.radius = radius
        self.normal = normal


class Polygon(object):

    def __init__(self, points):

        self.points = points