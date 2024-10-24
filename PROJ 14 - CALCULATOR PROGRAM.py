#program that simulates a calculator. it makes uses of functions, dictionaries, while loops and ifs

#for importing the ASCII art calculator logo
from calcu_resources import calc_logo

def add(n1,n2):
    '''function for adding numbers'''
    return n1+n2
def mult(n1,n2):
    '''function for multypling numbers'''
    return n1*n2
def subtr(n1,n2):
    '''function for subtracting numbers'''
    return n1-n2
def divi(n1,n2):
    '''funtion for dividing numbers'''
    return n1/n2

#dictionary for the operations. key will be the str that the users will input to choose which operation to do.
#values will be the functions defined above
operators={
    "+" : add,
    "-" : subtr,
    "*" : mult,
    "/" : divi
}

def calculator():
    '''function for the calc as a whole, for recursion purposes'''
    #boolean variable for the while loop
    repeat = True
    print(calc_logo)
    print("Welcome to the calculator program!")
    fnum = float(input("What's the first number: "))
    while repeat:
        
        operation = input("Choose operator: ( + - * / ): ")
        snum = float(input("What's the second number? "))
        #result variable will call the operators dictionary [key=operation] with (function values= fnum,snum)
        result = operators[operation](fnum,snum)
        print(f"{fnum} {operation} {snum} = {result}")

        #if choice is Y/y it will accumulate and continue calculating, so result=fnum then while loop will repeat until it becomes False
        choice = input(f"Type 'Y' to continue calculating with {result}, type 'N' to calculate from the beginning: ")
        if choice in ['Y','y']:
            fnum = result
        #when user inputs N/n, repeat will become False and then recursion of calculator function will occur to start from the beginning
        elif choice in ['n','N']:
            repeat = False
            calculator()
        #when user inputs anything other than the choices given, the program will end.
        else:
            print("Invalid Input! Ending the program")
            break

#calling the calculator function for starting the program.
calculator()