# n!=n×(n−1)×(n−2)×...×2×1

number= int(input("Enter number to calculate factorial: "))

print(f"Given Number is: {number}")

fact =1

for i in range(number,1,-1):
    fact = fact*i

print(f"Factorial is: {fact}")