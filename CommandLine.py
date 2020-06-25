import argparse # By importing this module we can pass parameters which is parsed using the parameters to the script.
if __name__=="__main__":
    parser=argparse.ArgumentParser(
        description="This is my math script"
    )
    # now we will add our arguments.
    # arguments are off two types.
    #1. Positional Arguments
    parser.add_argument("num1",help="ENter the number 1",type=float)
    parser.add_argument('num2',help ="enter no 2", type=float)
    parser.add_argument('operation',help="Enter an operator")

    args=parser.parse_args() # by this method the args will have all the arguments in the args variable
    print(args)
    result=None
    if args.operation == '+':
        result=args.num1 + args.num2
    elif args.operation=='-':
        if args.num1>=args.num2:
            result=args.num1-args.num2
        else:
            result=args.num2-args.num1
    elif args.operation == '*':
        result=args.num1*args.num2
    elif args.operation == '/':
        result=args.num1/args.num2
    elif args.operation == '^':
        result=pow(args.num1,args.num2)
    print("The result is ",result)
# for running the code open the terminal then type the following
 # python  ComandLine.py (value of ur choice) (value of ur choice) (operator of ur choice)

