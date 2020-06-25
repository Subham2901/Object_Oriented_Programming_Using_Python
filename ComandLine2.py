import argparse
if __name__=="__main__":
    parse=argparse.ArgumentParser(
        description= 'This script defines optional arguments'
    )
    # now we will write our optional arguments.
    parse.add_argument('-n1','--num1',help="Enter no 1",type=float,default=0)
    parse.add_argument('-n2','--num2',help='Enter no 2',type=float,default=0)
    parse.add_argument('-o','--operation',help="Enter an operator ",default='+')
    #
    args=parse.parse_args()
    result=None
    if args.operation=='+':
        result=args.num1+args.num2
    elif args.operation=='*':
        result=args.num1*args.num2
    elif args.operation=='/':
        result=args.num1/args.num2
    elif args.operation=='^':
        result=pow(args.num1,args.num2)
    elif args.operation=='-':
        if args.num1>=args.num2:
            result=args.num1-args.num2
        else:
            result=args.num2-args.num1
    print('The result is = ',result)
 # for running the code open the terminal then type the following
 # python  ComandLine2.py -n1=(value of ur choice) -n2=(value of ur choice) -o=(operator of ur choice)