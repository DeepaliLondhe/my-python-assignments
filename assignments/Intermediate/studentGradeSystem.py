# student grade system:

noOfStud = int(input("Enter no of Students:"))

def calGrade(total:int) ->str:
    avg= total/3
    if avg >=90:
        return "A+"
    elif avg>=70:
       return "A" 
    elif avg>=60:
       return "B"
    elif avg>=40:
        return "C"
    else:
        return "D"
    
Students = []

for i in range(noOfStud):
    name = input("Enter Student name:")
    rollno = int(input("Enter roll no."))
    marks = list(map(int,input("Enter marks of 3 subjects with comma seperated list:").split(",")))
    address = input("Enter adderss")
    total = sum(marks)
    grade = calGrade(total)

    student={
            "name": name,
            "rollno": rollno,
            "marks": marks,
            "total": total,
            "grade": grade,
            "address": address
    }
    Students.append(student)
   

print("Here is the student data:")

for s in Students:
    print (s)
