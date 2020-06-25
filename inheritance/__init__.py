import sys
import os
from time import sleep
from rectangle import rectangle
from square import square
from traingle import triangle
while(True):
    os.system('cls')
    print("-------------------------------------------------------")
    print("\tThe Polygon Area Finder")
    print("-------------------------------------------------------")
    print("1. To Check the area of a Rectangle.")
    print("2. To Check the area of a Triangle.")
    print("3. To Check the area of a Square.")
    print("-------------------------------------------------------")
    a=int(input("Enter your choice : "))

    if(a==1):
        r = rectangle()
        r.set_color()
        r.disp_color()
        r.disp()
        sleep(3)
        print("Press 1 to resume the code")
        print("Press any other key to exit")
        b = int(input("Enter your choice :"))
        if (b != 1):

            os.system('cls')

            sys.exit("Good Bye... :-) ")
        else:
            continue

    elif(a==2):
        t = triangle()
        t.set_color()
        t.disp_color()
        t.disp()
        sleep(3)
        print("Press 1 to resume the code")
        print("Press any other key to exit")
        b = int(input("Enter your choice :"))
        if (b != 1):

            os.system('cls')

            sys.exit("Good Bye... :-) ")
        else:
            continue
    elif(a==3):
        s = square()
        s.set_color()
        s.disp_color()
        s.disp()
        sleep(3)
        print("Press 1 to resume the code")
        print("Press any other key to exit")
        b = in1t(input("Enter your choice :"))
        if (b != 1):

            os.system('cls')

            sys.exit("Good Bye... :-) ")
        else:
            continue

    else:
        print("Your input is not valid\n")
        print("Press 1 to resume the code")
        print("Press any other key to exit")
        b=int(input("Enter your choice :"))
        if(b!=1):

            os.system('cls')

            sys.exit("Good Bye... :-) ")
        else:
            continue
















