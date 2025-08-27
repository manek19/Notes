#6.	Write a Python script to create a Student’s Marksheet.

student_name = input("Enter the student's name: ")
roll_number = input("Enter the roll number: ")
subject1 = input("Enter the name of subject 1: ")
subject2 = input("Enter the name of subject 2: ")
subject3 = input("Enter the name of subject 3: ")
subject4 = input("Enter the name of subject 4: ")
subject5 = input("Enter the name of subject 5: ")

subject1_marks = float(input(f"Enter the marks obtained in {subject1}: "))
subject2_marks = float(input(f"Enter the marks obtained in {subject2}: "))
subject3_marks = float(input(f"Enter the marks obtained in {subject3}: "))
subject4_marks = float(input(f"Enter the marks obtained in {subject4}: "))
subject5_marks = float(input(f"Enter the marks obtained in {subject5}: "))

subjescts = [subject1, subject2, subject3, subject4, subject5]
marks = [subject1_marks, subject2_marks, subject3_marks, subject4_marks, subject5_marks]

total_marks = sum(marks)
average_marks = total_marks / len(marks)

percentage = (total_marks / (len(marks) * 100)) * 100
grade = None

if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B+'
elif percentage >= 60:
    grade = 'B'
elif percentage >= 50:
    grade = 'C'
elif percentage >= 40:
    grade = 'D'
else:
    grade = 'F'

# Displaying the Marksheet
print("\nStudent's Marksheet")
print("---------------------")
print(f"Name: {student_name}")
print(f"Roll Number: {roll_number}")
print("---------------------")
print("Subject\t\tMarks Obtained")
print("---------------------")
for subject, mark in zip(subjescts, marks):
    print(f"{subject}\t\t{mark}")
print("---------------------")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print("---------------------")
print("End of Marksheet")
print("---------------------")

print("Thank you for using the Student's Marksheet program!")