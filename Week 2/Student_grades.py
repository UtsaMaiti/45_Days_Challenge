class StudentInfo:
    def __init__(self,name):
        self.name=name
        self.grades=[]

    def getGrades(self,grade):
        if grade in range(0,101):
            self.grades.append(grade)
        else:
            print("!Invalid Input!")
    def getSum(self):
            return sum(self.grades)
    def getAvg(self):
        if self.grades:
            return sum(self.grades)/len(self.grades)
        else:
            print("No data entered yet!")
            return None
    def showGrades(self):
            gradeSum=self.getSum()
            gradeAvg=self.getAvg()
            if gradeAvg is not None:
                print("Name of the student : ",self.name)
                print("Grade of the student : ",self.grades)
                print("Total grade of the student : ",gradeSum)
                print("Average grade of the student : ",gradeAvg)
            else:
                print("No data entered!")           
stuName=input("Enter the name of the student : ")
Stu=StudentInfo(stuName)
stuGrade=int(input("Enter the grades of the student : "))
for i in range(stuGrade):
    grade=float(input(f"Grade: {i + 1} : "))
    Stu.getGrades(grade)
Stu.showGrades()