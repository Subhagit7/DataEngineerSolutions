int_number = int(input("Enter the number:"))

def fact(n):
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for num in range(1,n+1):
        result = result * num

    return result

print("Factorial of the entered number is: ", fact(int_number))