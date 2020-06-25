import ourmath
print(ourmath.add(3,5))
# Thus we can observe that we just want to call the method from ourmath.py module but its also printing
# The print statement along with it.
# To avoid such situations we use the condition
# if __name__=="__main__"
# This conditon decides the name of the (.py) file used as the module here.
# when we call the (ourmath.py) module from the module itself then its name becomes (__main__)
# and it prints all the code present there,along with executing the methods
# where as in case ,when the (ourmath.py) is called from outside the file itself the name
# becomes ("ourmath") thus then it just executes the function which is being called from the respective
#python file