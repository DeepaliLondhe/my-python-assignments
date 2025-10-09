# Find Largest number from given numbers


#convert given number strings into number list
noList = list(map(int,input("Enter the number list: ").split()))

print(noList)

largest = noList[0]

for no in noList:
    if no > largest:
       largest = no

print("Largest number is : ", largest)