from polygon import Polygon
from shape import shape
class triangle(Polygon,shape):# we are inheriting the properties of the two super classes here
    def __area2(self):
        __h=self.set_h()
        __w=self.set__w()
        __a=__h*__w/2
        return __a
    def disp(self):
        print("Enter the dimensions of the triangle whose area you want to calculate ")
        __d=self.__area2()
        print("The area of the triangle is : ",__d)

