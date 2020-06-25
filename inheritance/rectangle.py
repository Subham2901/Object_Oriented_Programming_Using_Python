from polygon import Polygon
from shape import shape
class rectangle(Polygon,shape):# we are inheriting the properties of the two super classes here
    def __area1(self):
        h=self.set_h()
        w=self.set__w()
        a=h*w
        return a

    def disp(self):
        print("Enter the dimensions of the rectangle whose area you want to calculate ")
        a=self.__area1()
        print("The area of the rectangle is = ",a)


