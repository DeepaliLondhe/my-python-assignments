# Sum of digits in a number::

number = input("Enter a number")
#digits = number.split()

print(f"Here is the number",number) # its still a string

sumofnumber =0

for digit in number:
    sumofnumber += int(digit)

print(f"Sum of number is:", sumofnumber)