# ============================================================
#                 EXAM CONSULTATION SCHEDULER
# ============================================================
# Console-based prototype for managing exam consultation requests.
# Note: Records are stored in memory and reset when the program closes.

students = []
appointments = []


def print_header(title):
    """Print a title surrounded by equal-sign borders."""
    width = 78
    print("\n" + "=" * width)
    print(title.center(width))
    print("=" * width)


def valid_student_id(student_id):
    """Check that a student ID is not empty and contains no spaces."""
    return bool(student_id) and not any(char.isspace() for char in student_id)


def get_student_id(prompt="Enter Student ID: "):
    """Ask for a valid student ID."""
    while True:
        student_id = input(prompt).strip()
        if valid_student_id(student_id):
            return student_id
        print("Invalid Student ID. Please enter an ID without spaces.")


def find_student(student_id):
    """Return the registered student with this ID, or None."""
    for student in students:
        if student["student_id"] == student_id:
            return student
    return None


def register_account():
    print_header("STUDENT REGISTRATION")

    student_id = get_student_id()
    if find_student(student_id):
        print("This Student ID is already registered.")
        return

    name = input("Enter Full Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    students.append({
        "student_id": student_id,
        "name": name
    })
    print("=" * 78)
    print("Registration successful!")


def add_appointment():
    print_header("REQUEST EXAM CONSULTATION")

    student_id = get_student_id()
    student = find_student(student_id)

    if student is None:
        print("Student ID not found. Please register first.")
        return

    subject = input("Enter Subject/Exam: ").strip()
    if not subject:
        print("Subject/Exam cannot be empty.")
        return

    concern = input("Enter Reason for Consultation: ").strip()
    if not concern:
        print("Reason cannot be empty.")
        return

    date = input("Preferred Date (e.g., 2026-11-05): ").strip()
    if not date:
        print("Date cannot be empty.")
        return

    time = input("Preferred Time (e.g., 1:00 PM): ").strip()
    if not time:
        print("Time cannot be empty.")
        return

    appointment = {
        "student_id": student_id,
        "student_name": student["name"],
        "subject": subject,
        "concern": concern,
        "date": date,
        "time": time,
        "status": "Pending"
    }
    appointments.append(appointment)

    print("=" * 78)
    print("Consultation request submitted successfully!")
    print("Status: Pending")


def display_appointment(appointment, number=None):
    """Display one appointment in a bordered detail view."""
    print("=" * 78)
    if number is not None:
        print(f" CONSULTATION REQUEST #{number}".center(78))
    else:
        print(" CONSULTATION REQUEST DETAILS".center(78))
    print("=" * 78)
    print(f"| {'Student ID':<18}: {appointment['student_id']:<53}|")
    print(f"| {'Student Name':<18}: {appointment['student_name']:<53}|")
    print(f"| {'Subject/Exam':<18}: {appointment['subject']:<53}|")
    print(f"| {'Reason':<18}: {appointment['concern']:<53}|")
    print(f"| {'Preferred Date':<18}: {appointment['date']:<53}|")
    print(f"| {'Preferred Time':<18}: {appointment['time']:<53}|")
    print(f"| {'Status':<18}: {appointment['status']:<53}|")
    print("=" * 78)


def view_appointments():
    print_header("ALL CONSULTATION REQUESTS")

    if not appointments:
        print("No consultation requests found.")
        return

    # Table layout similar to a simple console tracker.
    border = (
        "+" + "-" * 5 +
        "+" + "-" * 15 +
        "+" + "-" * 22 +
        "+" + "-" * 18 +
        "+" + "-" * 13 +
        "+" + "-" * 13 + "+"
    )
    print(border)
    print(
        f"| {'No.':<3} "
        f"| {'Student ID':<13} "
        f"| {'Student Name':<20} "
        f"| {'Subject/Exam':<16} "
        f"| {'Date':<11} "
        f"| {'Time':<11} |"
    )
    print(border)

    for index, appointment in enumerate(appointments, start=1):
        print(
            f"| {index:<3} "
            f"| {appointment['student_id'][:13]:<13} "
            f"| {appointment['student_name'][:20]:<20} "
            f"| {appointment['subject'][:16]:<16} "
            f"| {appointment['date'][:11]:<11} "
            f"| {appointment['time'][:11]:<11} |"
        )
        print(border)

    print(f"Total Requests: {len(appointments)}")


def view_my_requests():
    print_header("VIEW MY CONSULTATION REQUESTS")

    student_id = get_student_id()
    student = find_student(student_id)

    if student is None:
        print("Student ID not found. Please register first.")
        return

    found = [
        appointment for appointment in appointments
        if appointment["student_id"] == student_id
    ]

    if not found:
        print("You have no consultation requests.")
        return

    print(f"Student: {student['name']} ({student_id})")
    for number, appointment in enumerate(found, start=1):
        display_appointment(appointment, number)


def search_appointment():
    print_header("SEARCH CONSULTATION REQUEST")

    student_id = get_student_id("Enter Student ID to search: ")
    found = [
        appointment for appointment in appointments
        if appointment["student_id"] == student_id
    ]

    if not found:
        print("No consultation request found for this Student ID.")
        return

    for number, appointment in enumerate(found, start=1):
        display_appointment(appointment, number)


def update_appointment():
    print_header("UPDATE CONSULTATION SCHEDULE")

    if not appointments:
        print("No consultation requests available to update.")
        return

    view_appointments()
    try:
        number = int(input("Enter request number to update: ").strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if number < 1 or number > len(appointments):
        print("Request number not found.")
        return

    appointment = appointments[number - 1]
    print("Leave a field blank to keep its current value.")

    new_date = input(f"New Date [{appointment['date']}]: ").strip()
    new_time = input(f"New Time [{appointment['time']}]: ").strip()

    if new_date:
        appointment["date"] = new_date
    if new_time:
        appointment["time"] = new_time

    print("=" * 78)
    print("Consultation schedule updated successfully!")


def cancel_appointment():
    print_header("CANCEL CONSULTATION REQUEST")

    if not appointments:
        print("No consultation requests available to cancel.")
        return

    view_appointments()
    try:
        number = int(input("Enter request number to cancel: ").strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if number < 1 or number > len(appointments):
        print("Request number not found.")
        return

    appointment = appointments[number - 1]
    display_appointment(appointment, number)

    confirm = input("Are you sure you want to cancel this request? (Y/N): ").strip().upper()
    if confirm == "Y":
        appointments.pop(number - 1)
        print("Consultation request cancelled successfully.")
    else:
        print("Cancellation stopped. Request was not removed.")


def main_menu():
    while True:
        print_header("EXAM CONSULTATION SCHEDULER")
        print("1. Register Student")
        print("2. Request Exam Consultation")
        print("3. View All Consultation Requests")
        print("4. View My Requests")
        print("5. Search Request by Student ID")
        print("6. Update Consultation Schedule")
        print("7. Cancel Consultation Request")
        print("0. Exit")
        print("=" * 78)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_account()
        elif choice == "2":
            add_appointment()
        elif choice == "3":
            view_appointments()
        elif choice == "4":
            view_my_requests()
        elif choice == "5":
            search_appointment()
        elif choice == "6":
            update_appointment()
        elif choice == "7":
            cancel_appointment()
        elif choice == "0":
            print_header("THANK YOU FOR USING THE EXAM CONSULTATION SCHEDULER")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 0 to 7.")


if __name__ == "__main__":
    main_menu()
