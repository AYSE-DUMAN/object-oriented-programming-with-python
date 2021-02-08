from point import Point 

class LineSegment:
    
    def __init__(self, startX, startY, endX, endY):
        self.__startPoint = Point(startX, startY)
        self.__endPoint = Point(endX, endY)

    def getStartPoint(self):                                                       
        return self.__startPoint

    def getEndPoint(self):
        return self.__endPoint

    def length(self):
        return self.__startPoint.distance(self.__endPoint)

    # determines whether the line is paralel to the y axis 
    def isVertical(self):
        return self.__startPoint.getX()== self.__endPoint.getX()

    def isHorizontal(self):
        return self.__startPoint.getY() == self.__endPoint.getY()

    def slope(self):
        if self.isVertical():
             return float("inf")

        elif self.isHorizontal():
            return "Horizontal Line Segment"

        else:
              xDiff, yDiff = self.__startPoint.getDifferences(self.__endPoint)  
              slope = yDiff / xDiff
              return slope

    def __call__(self, varx):
        m = self.slope()
        y = self.__startPoint.getY() + m * (varx - self.__startPoint.getX())  # y = y1 + m(x-x1)  
        return y

    def __equation(self):
        m = self.slope()
        return "y = {} + {}(x - {} )".format(self.__startPoint.getY(), m,  self.__startPoint.getX())
    
    def __str__(self):
        return self.__equation()
        

if __name__ == "__main__":


    line = LineSegment(1,2,3,4)
    # y = line.__call__(12)
    y = line(12) # objeyi fonk gibi çağırırsak __call__() çalışır.
    print(y)
    print("line equation is: {} ".format(line))


