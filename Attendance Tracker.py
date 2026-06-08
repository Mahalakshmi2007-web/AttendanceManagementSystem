attendance = {}

def add_student():
    name = input("Enter student name: ")
    attendance[name] = "Absent"
    print("Student added successfully!")

def mark_attendance():
    name = input("Enter student name: ")
    
    if name in attendance:
        status = input("Present (P) or Absent (A): ")
        
        if status.upper() == "P":
            attendance[name] = "Present"
        else:
            attendance[name] = "Absent"
            
        print("Attendance updated.")
    else:
        print("Student not found!")

def view_attendance():
    print("\nAttendance Report")
    print("-" * 25)
    
    for student, status in attendance.items():
        print(student, ":", status)

while True:
    print("\n1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        view_attendance()
    elif choice == "4":
        break
    else:
        print("Invalid Choice")