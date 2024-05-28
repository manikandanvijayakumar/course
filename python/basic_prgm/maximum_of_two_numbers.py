#How to find maximum of two numbers
#using function method
def max_num(x,y):
    if (x > y):
        return x
    else:
        return y
    
a = int(input("a:"))
b = int(input("b:"))
max_num(a,b)

#using max function
a = 7
b = 8
max_num = max(a,b)
print(max_num)

#lambda function
max_num = lambda x,y: x if (x>y) else y
max_num(11,96)

#Ternary operator
a = 7
b = 8
print(a if a>b else b)