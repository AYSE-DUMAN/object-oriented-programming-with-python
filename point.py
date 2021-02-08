import math

class Point:

    # creates a point object
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    # shift the points
    def shift(self, incX, incY):
        self.__x += incX  
        self.__y += incY
    
    def getDifferences(self, otherPoint):
        xDiff = self.__x - otherPoint.getX()
        yDiff = self.__y - otherPoint.getY()
        return xDiff, yDiff   

    # Compute the these point distance
    def distance(self, otherPoint):
        xDiff, yDiff = self.getDifferences(otherPoint)
        return math.sqrt(xDiff **2 + yDiff **2)
    
    @staticmethod   
    def origin():
        return Point(0,0)

    def __str__(self):
        return "Point({},{})".format(self.__x, self.__y)

    def __len__(self):
        return len(self.__str__())
    
    def __lt__(self, otherPoint):
        first_mag = (self.__x ** 2) + (self.__y ** 2)
        second_mag = (otherPoint.__x ** 2) + (otherPoint.__y ** 2)
        return first_mag < second_mag

    def __eq__(self, otherPoint):
        return (self.__x == otherPoint.__x) & (self.__y == otherPoint.__y)

    def __mul__(self, otherPoint):
        return self.__x * otherPoint.getX() + self.__y * otherPoint.getY()
    
    def __truediv__(self, otherPoint):
        return self.__x / otherPoint.getX() + self.__y / otherPoint.getY()
    
    def __add__(self, otherPoint):
        return Point(self.__x + otherPoint.getX(), self.__y + otherPoint.getY())
    
    def __sub__(self, otherPoint):
        return Point(self.__x - otherPoint.getX(), self.__y - otherPoint.getY())
    

       
if __name__ == "__main__":
    
    p1 = Point(1,2)
    p2 = Point(3,4)
    dist = p1.distance(p2)
    origin = Point.origin()

    print("First point:{},{}".format(p1.getX(), p1.getY())) # first point
    print("Second point:{},{}".format(p2.getX(), p2.getY())) # second point
    print("Distance between point1 and point2:{}".format(dist))
    print("inner product : {} ".format(p1*p2))
    print("addition of points : {}".format(p1.__add__(p2)))
    print("subtraction of points : {}".format(p1.__sub__(p2)))
    print("division of points : {}".format(p1.__truediv__(p2)))
    print("Origin point: {}".format(origin))
    print("magnitute of first point greater than magnitute of second point : {}".format(p1.__lt__(p2)))
    print("First point is equal to second point : {}".format(p1.__eq__(p2)))
   
    


