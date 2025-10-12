class Employee:
    def __init__(self,employee_id,name,age,salary):
        self._employee_id=employee_id
        self.name=name
        self.age=age
        self._salary=salary

    def set_employee_id(self,employee_id):
        self._employee_id=employee_id
    def get_employee_id(self):
        return employee_id
    
    def set_salary(self,salary):
        self._salary=salary
    def get_salary(self):
        return salary
    def display(self):
        print("employee id:",self._employee_id)
        print("Name:",self.name)
        print("age:",self.age)
        print("salary:",self._salary)
    def __del__(self):
        print("employee of name",self.name,"is deleted")

'''e=Employee(101,'tanish',20 ,100000)
e.set_employee_id(102)
print("employee id:",e.get_employee_id)
e.display()
del(e)'''

class Manager(Employee):
    def __init__(self,employee_id,name,age,salary,department):
        super().__init__(employee_id,name,age,salary)
        self.department=department
    def display(self):
        super().display()
        print("employee department:", self.department)
'''m=Manager( 101, "tanish", 20, 100000, "HR")
m.display()'''

class Developer(Employee):
    def __init__(self,employee_id,name,age,salary,programming_language):
        super().__init__(employee_id,name,age,salary)
        self.programming_language= programming_language
    def display(self):
        super().display()
        print("programming language:",self.programming_language)
'''d=Developer(101,"tanish", 20, 100000, "python")
d.display()'''
m=Manager
print(" Manager is subclass of Employee", issubclass(m,Employee))
d=Developer
print(" Developer is subclass of Employee", issubclass(d,Employee))

#menu drive
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name, "Age:", self.age)

class employee(person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    def set_salary(self, salary):
        self.salary = salary

    def display(self):
        super().display()
        print("Employee ID:", self.employee_id, "Salary:", self.salary)

class manager(employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)

people = []

while True:
    print("\n--- Python OOP Project: Employee Management System ---")
    print("Choose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    match choice:
        case '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            p = person(name, age)
            people.append(p)
            print(f"Person created with Name: {name} and Age: {age}")

        case '2':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            e = employee(name, age, employee_id, salary)
            people.append(e)
            print(f"Employee created with Name: {name}, Age: {age}, ID: {employee_id}, Salary: {salary}")

        case '3':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            department = input("Enter Department: ")
            m = manager(name, age, employee_id, salary, department)
            people.append(m)
            print(f"Manager created with Name: {name}, Age: {age}, ID: {employee_id}, Salary: {salary}, Department: {department}")

        case '4':
            print("Choose detail to show")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            choice2 = input("Enter your choice: ")

            if choice2 == '1':
                print("Person details:")
                for p in people:
                    if isinstance(p, person) and not isinstance(p, employee):
                        p.display()

            elif choice2 == '2':
                print("Employee details:")
                for e in people:
                    if isinstance(e, employee) and not isinstance(e, manager):
                        e.display()

            elif choice2 == '3':
                print("Manager details:")
                for m in people:
                    if isinstance(m, manager):
                        m.display()

            else:
                print("Invalid choice")

        case '5':
            print("Exiting the system. All resources are freed.")
            print("Goodbye!")
            break

        case _:
            print("Invalid choice.")




        
    
    
