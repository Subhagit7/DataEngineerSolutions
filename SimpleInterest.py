P = float(input("Enter the principal amount:"))
R = float(input("Enter the rate of interest:"))
T = float(input("Enter the tenure:"))

def SimpleInterest(a, b, c):
    return (a * b * c) / 100

print("Derrived Simple Interest is: ", SimpleInterest(P, R, T))
