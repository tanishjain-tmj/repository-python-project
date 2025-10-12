import os

def menu():
    while True:
        print("\nFile Operations Menu")
        print("1. Create a File")
        print("2. Read a File")
        print("3. Delete a File")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter file name to create: ")
            content = input("Enter text to write: ")
            with open(filename, "w") as f:
                f.write(content)
            print(f"File '{filename}' created successfully!")

        elif choice == '2':
            filename = input("Enter file name to read: ")
            with open(filename, "r") as f:
                print("File content:\n")
                print(f.read())

        elif choice == '3':
            filename = input("Enter file name to delete: ")
            os.remove(filename)
            print(f"File '{filename}' deleted successfully.")
            

        elif choice == '4':
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice, try again.")
