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
    print("student added successfully!")
def displayData():
    if(students.count == 0):
        print("list is empty")
    for index,student in enumerate(students,1):
        print(f"Name:{student['name']}")
        print(f"Age:{student['age']}")
        print(f"rollno:{student['rollno']}")
        print()
def removeData():
    student_remove=input("Enter the student to remove:")
    for student in students:
        # if student[] == student_remove:
            students.remove()
getData()
displayData()
def main():
    while True:
        print("Choices:")
        print("1.Add student:")
        print("2.Display student:")
        print("3.Remove student:")
        print("4.Exit")
        choice = input("Enter Your Choice(1-4):")
        if choice == 1:
            getData()
        elif choice == 2:
            displayData()

            
        
        
    