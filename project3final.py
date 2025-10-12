while True:
    print("welcome to the student data organizer!")
    print()
    print("select an option:")
    print("1.Add Student\n2.Display all students\n3.Update student information\n4.Delete student\n5.Display subject offered\n6.Exit")

    Choice = int(input("enter your choice:"))

    match Choice:
        case 1:
             print("Enter student detail:")
             student_id=int(input("student_id:"))
             name=str(input("name:"))
             age=int(input("age:"))
             grade=str(input("Grades:"))
             date_of_birth=input("Date_of_birth(YYYY-MM-DD)")
             subject=input("Subject:")

             print("Student added successfully")

        case 2:
             print("---Display all students---")
             print("")
        
        
        
        
