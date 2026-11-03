# Exam-Consultation-Scheduler-

print("--- Appointment Scheduler ---")

students = []
appointments = []

def valid_student_id(student_id):
    has_digit = False
    for character in student_id:
        if character >= "0" and character <= "9":
            has_digit = True
        elif character != "-":
            return False
    return has_digit

def get_student_id(message):
    student_id = input(message)
    if student_id == "":
        print("Please enter a Student ID.")
        return ""
    if valid_student_id(student_id) == False:
        print("Invalid Student ID. Use numbers and hyphens only.")
        return ""
    return student_id

def find_student(student_id):
    for student in students:
        if student[0] == student_id:
            return student
    return None

def register_account():
    print("\n--- Register Student ---")
    student_id = get_student_id("Enter student ID: ")
    if student_id == "":
        return
    student_name = input("Enter student name: ")
    has_letter = False
    for character in student_name:
        if ("A" <= character <= "Z") or ("a" <= character <= "z"):
            has_letter = True
        elif "0" <= character <= "9":
            print("Invalid student name. Do not use numbers.")
            return
    if student_name == "" or has_letter == False:
        print("Please enter a valid student name.")
        return
    if find_student(student_id) != None:
        print("Student ID already registered.")
        return
    students.append([student_id, student_name])
    print("Student registered successfully!")

def add_appointment():
    print("\n--- Submit Consultation Request ---")
    student_id = get_student_id("Enter student ID: ")
    if student_id == "":
        return
    student = find_student(student_id)
    if student == None:
        print("Student ID not found. Please register first.")
        return
    subject = input("Enter subject or exam: ")
    concern = input("Enter reason for consultation: ")
    if subject == "" or concern == "":
        print("Please complete the required information.")
        return
    appointments.append([student_id, student[1], subject, concern,
                         "Not scheduled", "Not scheduled"])
    print("Consultation request submitted successfully!")
    print("The teacher will set the date and time.")

def display_appointment(appointment, number):
    print("\nAppointment", number)
    print("Student ID:", appointment[0])
    print("Student Name:", appointment[1])
    print("Subject or Exam:", appointment[2])
    print("Reason:", appointment[3])
    print("Consultation Date:", appointment[4])
    print("Consultation Time:", appointment[5])

def view_appointments():
    if len(appointments) == 0:
        print("\nNo consultation requests recorded.")
        return
    print("\n--- All Consultation Requests ---")
    number = 1
    for appointment in appointments:
        display_appointment(appointment, number)
        number = number + 1
def show_student_requests(student_id):
    found = False
    number = 1
    for appointment in appointments:
        if appointment[0] == student_id:
            display_appointment(appointment, number)
            found = True
        number = number + 1
    if found == False:
        print("No consultation request found.")
def view_my_requests():
    student_id = get_student_id("\nEnter your Student ID: ")
    if student_id == "":
        return
    if find_student(student_id) == None:
        print("Student ID not found. Please register first.")
        return
    print("\n--- Your Consultation Requests ---")
    show_student_requests(student_id)
def search_appointment():
    student_id = get_student_id("\nEnter Student ID to search: ")
    if student_id == "":
        return
    print("\n--- Search Results ---")
    show_student_requests(student_id)

def update_appointment():
    print("\n--- Set or Reschedule Consultation ---")
    appointment_number = input("Enter appointment number: ")
    if appointment_number == "":
        print("Please enter an appointment number.")
        return
    number = 1
    for appointment in appointments:
        if str(number) == appointment_number:
            display_appointment(appointment, number)
            new_date = input("Enter date (e.g., September 26, 2026): ")
            new_time = input("Enter time (e.g., 1:00 PM): ")
            if new_date == "" or new_time == "":
                print("Date and time are required.")
                return
            appointment[4] = new_date
            appointment[5] = new_time
            print("Consultation schedule saved successfully!")
            return
        number = number + 1
    print("No consultation request found for that number.")

def cancel_appointment():
    print("\n--- Cancel Consultation Request ---")
    appointment_number = input("Enter appointment number to cancel: ")
    if appointment_number == "":
        print("Please enter an appointment number.")
        return
    number = 1
    for appointment in appointments:
        if str(number) == appointment_number:
            display_appointment(appointment, number)
            confirm = input("Cancel this request? (Y/N): ")
            if confirm == "Y" or confirm == "y":
                appointments.pop(number - 1)
                print("Consultation request cancelled successfully!")
            elif confirm == "N" or confirm == "n":
                print("Cancellation stopped. The request was kept.")
            else:
                print("Invalid input. Please enter Y or N.")
            return
        number = number + 1
    print("No consultation request found for that number.")
def student_menu():
    while True:
        print("\n--- STUDENT MENU ---\n1. Register Account\n2. Submit Consultation Request\n3. View My Requests\n4. Return")
        choice = input("Choose an option: ")
        if choice == "1":
            register_account()
        elif choice == "2":
            add_appointment()
        elif choice == "3":
            view_my_requests()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose 1-4.")
def teacher_menu():
    while True:
        print("\n--- TEACHER MENU ---\n1. View All Requests\n2. Search by Student ID\n3. Set or Reschedule Date and Time\n4. Cancel Request\n5. Return")
        choice = input("Choose an option: ")
        if choice == "1":
            view_appointments()
        elif choice == "2":
            search_appointment()
        elif choice == "3":
            update_appointment()
        elif choice == "4":
            cancel_appointment()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose 1-5.")

def main_menu():
    while True:
        print("\n--- APPOINTMENT SCHEDULER ---\n1. Student\n2. Teacher\n3. Exit")
        choice = input("Choose your role: ")
        if choice == "1":
            student_menu()
        elif choice == "2":
            teacher_menu()
        elif choice == "3":
            print("Thank you for using Appointment Scheduler!")
            break
        else:
            print("Invalid choice. Please choose 1-3.")

main_menu()
