#How to find factorial of numbers
#using looping function
n = 5
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)

#using function 
def factorial(n):
    return 1 if (n == 0 or n == 1) else n*factorial(n-1)
factorial(6)

#Recursive function 
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    elif (n < 0):
        return 0
    else:
        fact = 1
        while (n>1):
            fact *= n
            n -= 1
        return fact
factorial(5)

#math module
import math

fact = factorial(5)
print(fact)