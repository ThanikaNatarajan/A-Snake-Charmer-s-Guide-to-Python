
#USER DEFINED FUNCTIONS

'''
User defined functions are maded by users for their own use in the program 
It can be used in any part of the program by invoking/calling it 
It is defined using the keyword "def"

SYNTAX 
def function_name():
    statement(s)

Parameters : Values given in the function definition ---> aka formal parameter (or) formal arguments - parameters that are recieved 
Arguments : Values given in the function call        ---> aka actual parameter (or) actual arguments - parameters that are passed  
'''

# Q.1 Write a function to find the sum of 2 numbers (NO parameter , NO return) 
def add():
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    z=a+b
    print("Sum is :" , z)
add()  

 #Q.2 Write a function to find the sum of 2 numbers ( NO parameter , with return)
def add_return():
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    z=a+b
    return z

result=add()
print("The sum is :" , result)

# Q.3 Write a function to find the sum of 2 numbers ( with parameter , NO return)
def add_para(a,b):                                         # a,b are formal parameters / formal arguments / parameters 
    z=a+b
    print("Sum is :" , z)
n1=int(input("Enter first number : "))
n2=int(input("Enter second number : "))
add(n1,n2)                                                 # n1,n2 are actual parameters / actual arguments / arguments 


# Q.4 Write a function to find the sum of 2 numbers ( with parameter , with return)
def add_para_return(a,b):
    z=a+b
    return z

n1=int(input("Enter first number : "))
n2=int(input("Enter second number : "))
result=add(n1,n2)
print(result)
