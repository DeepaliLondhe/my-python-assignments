Name = input("Enter a string to reverse it:")
print("Original string is "+ Name)

# using slicing
print("Reverse string using slicing is: ", Name[::-1])

# using char by char reversed
reversedtext = " "

for char in Name:
    reversedtext = char+reversedtext

print("Reverse string using char by char is "+ reversedtext)

