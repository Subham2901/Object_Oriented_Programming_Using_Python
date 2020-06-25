from polygon import Polygon
from shape import shape
class square(Polygon,shape):# we are inheriting the properties of the two super classes here
    def __area2(self):
        __s=self.set__s()
        a=__s**2
        return a
    def disp(self):
        print("enter the side of the square  whose area you want to calculate")
        __d=self.__area2()
        print("The area of the square is : ",__d)
