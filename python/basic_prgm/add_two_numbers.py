#How to add numbers in Python
#using function method
def addition (x,y):
    z=x+y
    return z

addition(38,55)

#lambda function
addition = lambda a,b: a+b
addition(4,7)

#operator method
import operator
x=10
y=30
addition = operator.add(x,y)
print(addition)

#Recursive methon
def recursive_addition(x,y):
    if(y==0):
        return x
    else:
        return recursive_addition(x+1,y-1)
result = recursive_addition(22,11)
print(result)