# Find Largest number from given numbers:

noList = list(map(int,input("Enter the number list: ").split()))

print(noList)

largest = noList[0]

for no in noList:
    if no > largest:
       largest = no

print("Largest number is : ", largest)