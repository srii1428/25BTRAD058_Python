# Student grading system.
#* Student Grading System: Develop a Python program to store student names
#and marks using dictionaries, calculate grades using conditional statements,
#and display results.
#* Apply conditional logic, analyze grade boundaries, and verify results
# using test cases. (CT)
#* Simulate an academic grading scenario and interpret student
#performance results. (RWE)

students = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
students[name] = marks
for name in students:
    marks = students[name]
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"
        print(name, marks, grade)