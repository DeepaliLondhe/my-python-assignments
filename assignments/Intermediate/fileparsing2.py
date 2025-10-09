inputFile = open("inputFile.txt","r") 
passFile = open("passFile.txt","w") 
failFile = open("failFile.txt","w") 

for line in inputFile:
    fileLine=line.split()
    if fileLine[2] == "P":
        passFile.write(line)
    else:
        failFile.write(line)
    print(line)

#print ("Data from passfile is here:")
#for passline in inputFile:
#   print(passline)

#print ("Data from failFile is here:")
#for failline in inputFile:
#   print(failline)


inputFile.close()
passFile.close()
failFile.close()