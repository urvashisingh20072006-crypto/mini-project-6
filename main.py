# Student Records Persistence & Export System

import json
import csv
import os
from datetime import datetime

def show_menu():
    print("\n==== STUDENT RECORDS SYSTEM ====")
    print(""" 
    1.Add Student 
    2.Search Student
    3.View all students
    4.Export record to csv
    5.View activity log
    6.Exit
        """)

    while True:
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            view_all_students()
        elif choice == '4':
            export_to_csv()
        elif choice == '5':
            view_activity_log()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def add_student():
    student = {}
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    department = input("Enter Student Department: ")
    python_marks = input("Enter Student Python Marks: ")
    maths_marks = input("Enter Student Maths Marks: ")
    ds_marks = input("Enter Student Data Structures Marks: ")

    student[student_id] = {
        "name": student_name,
        "department": department,
        "marks": {
            "python": python_marks,
            "maths": maths_marks,
            "DS": ds_marks
        }
    }

    with open('students.json', 'a') as f:
        f.write(json.dumps(student) + '\n')

    log_activity(f"Added student: {student[student_id]} - {student[student_id]['name']}")
    print(f"Student {student[student_id]['name']} added successfully.")

def search_student():
    student_id = input("Enter Student ID to search: ")
    found = False

    if os.path.exists('students.json'):
        with open('students.json', 'r') as f:
            for line in f:
                student = json.loads(line)
                if student_id in student:
                    print(f"Student Found: {student[student_id]}")
                    found = True
                    break

    if not found:
        print("Student not found.")

    log_activity(f"Searched for student ID: {student_id}")

def view_all_students():
    if os.path.exists('students.json'):
        with open('students.json', 'r') as f:
            print("\nAll Students:")
            for line in f:
                student = json.loads(line)
                for student_id in student:
                    print(student[student_id])
    else:
        print("No student records found.")

    log_activity("Viewed all students")

def export_to_csv():
    if os.path.exists('students.json'):
        with open('students.json', 'r') as f:
            students_data = json.load(f)

        with open('students.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'name', 'department', 'python', 'maths', 'DS']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for student_id, student_info in students_data.items():
                row = {
                    'id': student_id,
                    'name': student_info['name'],
                    'department': student_info['department'],
                    'python': student_info['marks']['python'],
                    'maths': student_info['marks']['maths'],
                    'DS': student_info['marks']['DS']
                }
                writer.writerow(row)

        print("Student records exported to students.csv")
        log_activity("Exported student records to CSV")
    else:
        print("No student records found to export.")

def view_activity_log():
    if os.path.exists('activity_log.txt'):
        with open('activity_log.txt', 'r') as f:
            print("\nActivity Log:")
            for line in f:
                print(line.strip())
    else:
        print("No activity log found.")

    log_activity("Viewed activity log")

def log_activity(activity):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('activity_log.txt', 'a') as f:
        f.write(f"{timestamp} - {activity}\n")

    


if __name__ == "__main__":
    show_menu()