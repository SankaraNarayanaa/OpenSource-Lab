import Student

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        Student.add_student()

    elif choice == "2":
        Student.display_students()

    elif choice == "3":
        Student.search_student()

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Please try again.")
