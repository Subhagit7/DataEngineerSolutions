P = float(input("Enter the principal amount:"))
R = float(input("Enter the rate of interest:"))
T = int(input("Enter the tenure:"))

def CompoundInterest(a, b, c):
    return a * (1+ b/100)**c

print("Derrived Simple Interest is: ", CompoundInterest(P, R, T))