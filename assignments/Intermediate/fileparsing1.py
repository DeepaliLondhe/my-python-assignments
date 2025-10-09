OpenFile = open("inputFile.txt","r")

for line in OpenFile:
    print(line)

OpenFile.close()