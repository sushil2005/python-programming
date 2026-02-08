students = []

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks (0 - 100): "))

    student = {
        "name": name,
        "marks": marks
    }
    students.append(student)
    print("Student added successfully!\n")


def calculate_grade(marks):
    return (lambda m:
            "A" if m >= 80 else
            "B" if m >= 60 else
            "C" if m >= 40 else
            "F")(marks)


def show_all_students():
    if not students:
        print("No student records found.\n")
        return

    for s in students:
        print(f"Name: {s['name']} | Marks: {s['marks']} | Grade: {calculate_grade(s['marks'])}")
    print()


def sort_students():
    if not students:
        print("No data to sort.\n")
        return

    sorted_list = sorted(students, key=lambda x: x["marks"], reverse=True)
    for s in sorted_list:
        print(f"{s['name']} - {s['marks']}")
    print()


def filter_pass_students():
    passed = list(filter(lambda x: x["marks"] >= 40, students))

    if not passed:
        print("No passed students.\n")
        return

    for s in passed:
        print(f"{s['name']} - {s['marks']}")
    print()


def menu():
    while True:
        print("===== Student Result System =====")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Sort Students by Marks")
        print("4. Show Passed Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_all_students()
        elif choice == "3":
            sort_students()
        elif choice == "4":
            filter_pass_students()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.\n")


menu()
