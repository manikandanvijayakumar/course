# Note:
# P -> Principal
# T -> Time line
# r -> rate of interest

# Formula:
#     A = P(1+R/100)t
#     ci = A-P

#Using function with pow
P = int(input("Enter Principal amount: "))
R = int(input("Enter Rate of interest: "))
T = int(input("Enter Timeline: "))

def intrest_cal (P,T,R):
    A = P*(pow((1+R/100),T))
    ct = A-P
    return ct

intrest_cal(P,T,R)

#without use power
P = 10000
R = 10
T = 5
A = P*(1+(R/100))**T
ct = A-P
print(ct)

#using looping function
def intrest_cal (P,T,R):
    A = P
    
    for i in range(T):
        A = A*(1+R/100)
        CI = A-P
    return CI

intrest_cal(1200,2,5.4)
