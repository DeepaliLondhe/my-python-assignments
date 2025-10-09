# creating grading concept for again but this time with class:

class student:
    def __init__(self,name,rollno,marks,address):
            self.name = name 
            self.rollno = rollno
            self.marks = marks
            self.address = address
            self.total =0
            self.grade = None

    def calTotal(self):
        self.total = sum(self.marks)

    def calGrade(self):
         avg = self.total/len(self.marks)
         if avg >=90:
              self.grade ="A+"
         elif avg >=80:
              self.grade ="A"
         elif avg >=65:
              self.grade ="B"
         elif avg >=40:
              self.grade ="C"
         else:
            self.grade ="Fail"