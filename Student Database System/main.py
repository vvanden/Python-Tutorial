# Create an empty list to store instances of the Student class
students = []

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade, index=None):
        if index is None:
            self.grades.append(grade)
        else:
            if 0 <= index < len(self.grades):
                self.grades[index] = grade
            else:
                print("Invalid index. Grade not updated.")

    def average_grade(self):
        if len(self.grades) == 0:
            return "No grades available"
        else:
            return round(sum(self.grades) / len(self.grades),1)

# Function to find a student by name
def find_student_by_name(name):
    for student in students:
        if student.name == name:
            return student
    return None

#setting initial condition
req_active = True

while req_active:
    req = input("Student Grade Database, would you like to add (S)tudent, (G)rades, display (A)varage, (E)xit:")
    if req == "S" or req == "s":
        name = str(input("Please enter student name: "))
        while True:
            try:
                age = int(input("Please enter student age: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                break
        students.append(Student(name, age))
    elif req == "G" or req == "g":
        student_name = input ("Input student name:")
        student = find_student_by_name(student_name)
        if student:
            while True:
                try:
                    student_grade = int(input ("Input student grade:" ))
                except ValueError:
                    print("Sorry, I didn't understand that.")
                    continue
                else:
                    break
            student.add_grade(student_grade)
        else:
            print(f"Student with name '{student_name}' not found.")
    elif req == "A" or req == "a":
        student_name = input ("Input student name:")
        student = find_student_by_name(student_name)
        if student:
            average_grade = student.average_grade()    
            print(f"Grades for {student_name}: {student.grades} {average_grade}")
        else:
            print(f"Student with name '{student_name}' not found.")
    elif req == "E" or req == "e":
        print("Good bye.")
        req_active = False
    else:
        print("Sorry, I didn't understand that.")