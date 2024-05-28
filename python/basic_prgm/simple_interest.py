# Note:
# P -> Principal
# T -> Time line
# r -> rate of interest

# Formula:
#     = (P*T*R)/100

P = int(input("Enter Principal amount: "))
R = int(input("Enter Rate of interest: "))
T = int(input("Enter Timeline: "))

def interest_cal (P,T,R):
    result = (P*T*R)/100
    return result

interest_cal(P,T,R)