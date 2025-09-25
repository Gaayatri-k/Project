import csv
import os
import sys
import statistics
Filename="studentsmanagement.csv"
Deletedfile="students_deleted.csv"
Reportfolder="reports"
def read_students():
    if not os.path.exists():
        with open(Filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Roll_No","Name","Branch","Year","Gender","Age",
                             "Attendance","Mid1","Mid2","Quiz","Final"])
    with open(Filename, newline="") as f:
        return list(csv.DictReader(f))
def write_students(students):
    with open(Filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=students[0].keys())
        writer.writeheader()
        writer.writerows(students)
def ensure_reports_folder():
    if not os.path.exists(Reportfolder):
        os.makedirs(Reportfolder)
def add_student():
    students = read_students()
    roll = input("Enter Roll No: ")
    if any(s["Roll_No"] == roll for s in students):
        print("Duplicate Roll No.")
        return
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    year = input("Enter Year: ")
    gender = input("Enter Gender: ")
    age = input("Enter Age: ")
    attendance = input("Enter Attendance %: ")
    mid1 = input("Mid1 Marks: ")
    mid2 = input("Mid2 Marks: ")
    quiz = input("Quiz Marks: ")
    final = input("Final Marks: ")
    new_student = {
        "Roll_No": roll, "Name": name, "Branch": branch, "Year": year,
        "Gender": gender, "Age": age, "Attendance": attendance,
        "Mid1": mid1, "Mid2": mid2, "Quiz": quiz, "Final": final
    }
    students.append(new_student)
    write_students(students)
    print("Student added successfully.")