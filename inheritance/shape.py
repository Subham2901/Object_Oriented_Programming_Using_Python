class shape():# super class
    __color=None
    def set_color(self):
        self.__color=input("Enter the color  of the figure:")
    def get_color(self):
        return self.__color
    def disp_color(self):
        print(" The color that you have entered is :",self.get_color())
