def fact_module(n):
    if (n == 0 or n == 1):
        return 1 
    elif n < 0:
        return 0
    else:
        fact = 1
        for i in range(1,n+1):
            fact = fact * i
        return fact

print(fact_module(5))