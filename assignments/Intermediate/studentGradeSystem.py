# student grade system:

noOfStud = int(input("Enter no of Students:"))

Students = []

for i in range(noOfStud):
    name = input("Enter Student name:")
    rollno = int(input("Enter roll no."))
    marks = int(input("Enter marks:"))
    add = input("Enter adderss")

    student={
            "name": name,
            "rollno": rollno,
            "marks": marks,
            "add": add
    }
    Students.append(student)

print("Here is the student data:")

for s in Students:
    print (s)


