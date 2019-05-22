from point import Point

class Line(object):

    def __init__(self, start, end):

        self.start = start
        self.end   = end
    
    def project_from(self, point):

        base = self.end - self.start
        r    = (point - self.start) * base / base.norm

        return self.start + base * r

    def reflect_from(self, point):

        return point + (self.project_from(point) - point) * 2

    def distance_from_point(self, point, as_segment=False):

        base = self.end - self.start

        if as_segment:
            
            if (point - self.start) * base < 0:

                # outside

                return (point - self.start).length
            
            elif (point - self.end) * base < 0:

                # outside

                return (point - self.end).length

            else:

                # inside

                self.distance_from(point, False)

        else:

            # The magnitude of the cross product equals the area of a parallelogram with the vectors for sides
            area = (self.end - self.start).cross_product(point - self.start).length
            return area / (self.end - self.start).length

    def distance_from_line(self, line, as_segment=False):

        # Referenced http://paulbourke.net/geometry/pointlineplane/ as well

        d = lambda m, n, o, p: (m.x - n.x) * (o.x - p.x) + (m.y - n.y) * (o.y - p.y) + (m.z - n.z) * (o.z - p.z)

        d1343 = d(self.start, line.start, line.end, line.start)
        d4321 = d(line.end, line.start, self.end, self.start)
        d1321 = d(self.start, line.start, self.end, self.start)
        d4343 = d(line.end, line.start, line.end, line.start)
        d2121 = d(self.end, self.start, self.end, self.start)

        a = (d2121 * d4343 - d4321 * d4321)

        if a == 0:

            # in case lines are pararrel, get the shortest distance between the ends of each line

            d1 = self.distance_from_point(line.start, as_segment=as_segment)
            d2 = self.distance_from_point(line.end, as_segment=as_segment)
            d3 = line.distance_from_point(self.start, as_segment=as_segment)
            d4 = line.distance_from_point(self.end, as_segment=as_segment)

            return min(min(d1, d2), min(d3, d3)) 

        else:

            mua = (d1343 * d4321 - d1321 * d4343) / (d2121 * d4343 - d4321 * d4321)
            mub = (d1343 + mua * d4321) / d4343

            if not as_segment or (0 <= mua and mua <= 1 and 0 <= mub and mub <= 1):
        
                pa = self.start + (self.end - self.start) * mua
                pb = line.start + (line.end - line.start) * mub

                # cast from vector to point
                pa = Point(pa.x, pa.y, pa.z)
                pb = Point(pb.x, pb.y, pb.z)

                dist = pa.distance_to(pb)

                return dist

            d1 = self.distance_from_point(line.start, as_segment=as_segment)
            d2 = self.distance_from_point(line.end, as_segment=as_segment)
            d3 = line.distance_from_point(self.start, as_segment=as_segment)
            d4 = line.distance_from_point(self.end, as_segment=as_segment)

            return min(min(d1, d2), min(d3, d3)) 


    def __repr__(self):
        
        return str(self)

    def __str__(self):
        
        return 'L(%s, %s)' % (self.start, self.end)


class Circle(object):

    def __init__(self, center, radius, normal):

        self.center = center
        self.radius = radius
        self.normal = normal


class Polygon(object):

    def __init__(self, points):

        self.points = points


if __name__ == '__main__':

    from point import Point

    p0 = Point(0, 0, 0)
    p1 = Point(10, 0, 0)
    p2 = Point(5, 5, 0)
    p3 = Point(-1, -1, 0)

    print('p0: ', p0)
    print('p1: ', p1)
    print('p2: ', p2)
    print('p3: ', p3)

    print('-' * 30)

    line = Line(p0, p1)
    
    projected = line.project_from(p2)
    reflected = line.reflect_from(p2)

    print('Point ', p2, ' is projected to ', projected, ' on line ', line)
    print('Point ', p2, ' is reflected to ', reflected, ' on line ', line)

    print('-' * 30)

    print('The distance between p3 and L(p0, p1) is', line.distance_from_point(p3))
    print('The distance between p3 and S(p0, p1) is', line.distance_from_point(p3, as_segment=True))


    print('-' * 30)

    line1 = Line(Point(0, 0, 0), Point(10, 0, 0))
    line2 = Line(Point(0, 10, 0), Point(10, 10, 0))

    print('distance between %s and %s ='  % (line1, line2), line1.distance_from_line(line2))

    line3 = Line(Point(0, 0, 0), Point(10, 0, 0))
    line4 = Line(Point(0, 0, 0), Point(10, 0, 0))

    print('distance between %s and %s =' % (line3, line4), line3.distance_from_line(line4))


    line5 = Line(Point(10, 10, 10), Point(-10, -10, -10))
    line6 = Line(Point(10, -10, 10), Point(-10, 10, -10))

    print('distance between %s and %s =' % (line5, line6), line5.distance_from_line(line6))

    line7 = Line(Point(0, 0, 0), Point(1, 2, -4))
    line8 = Line(Point(-10, -5, 0), Point(10, 5, 3))
    
    print('distance between %s and %s =' % (line7, line8), line7.distance_from_line(line8))
