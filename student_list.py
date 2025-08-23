# student_list=[] 

# name = input("Enter Your Name:" )
# age = input("Enter Your Age:")
# rollno = input("Enter Your Rollno:")

# class Student:
#     def __init__(self,name,age,rollno):
#         self.name=name
#         self.age=age
#         self.rollno=rollno
#         student_list.append(self)
#         print(f"student {self.name} appended.")
#         print("students:",student_list)
#     # def __init__(self):
#     #     Student.append(self)
#     #     print(f"{Student} Appended")
#     #     print("student:",Student)
students=[]
def getData():
    name=input("enter your name:")
    age=input("enter your age:")
    rollno=input("enter your rollno:")
    student = {
        "name": name,
        "age":age,
        "rollno":rollno
    }
    students.append(student)
    print("student added successfully")
def displayData():
    if(students.count == 0):
        print("list is empty")
    for index,student in enumerate(students,1):
        print(f"Name:{student}")
        print()
def main():
    print(" ")
    choice =input("Enter your choice")
    if (choice == 1):
        getData()
    else:
        displayData()
main() 
        
    
