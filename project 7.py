import datetime , math, random,uuid,time,sys,string

try:
    import file_operations
except Exception:
    print("ERROR: 'file_operations.py'not found ")


def datetime_operation():
    while True:
        print("Datetime and Time operations:")
        print("1.Display current date and time")
        print("2.calculate differences between two dates/time")
        print("3.Format date into custom format")
        print("4.Stopwatch")
        print("5.countdown timer")
        print("6.back to main menu")

        c=int(input("Enter your choice:"))
        if c==1:
            print("Current date and time:",datetime.datetime.now())
        elif c==2:
            date_1=datetime.datetime.strptime(input("Enter date1(YYYY-MM-DD):"),"%Y-%m-%d")
            date_2=datetime.datetime.strptime(input("Enter date2(YYYY-MM-DD):"),"%Y-%m-%d")
    
            difference=(abs(date_2 - date_1).days)
            print("differences between two dates:",difference)
        elif c==3:
            date=datetime.datetime.strptime(input("Enter date(YYYY-MM-DD):"),"%Y-%m-%d")
            format= input("Enter format:")
            print("formatted date:",date.strftime(format))
        elif c==4:
            input("press Enter to start:")
            start=time.time();
            input("press enter to stop:")
            print(f"Elapsed:{time.time()-start:.2f} sec")
        elif c==5:
            t=int(input("Enter seconds:"))
            while t>0:
                print(t)
                time.sleep(1)
                t-=1
            print("time's up")
        elif c==6:
            print("back to main menu:")
            break
        else:
            print("Invalid choice, try again.")

def math_operation():
    while True:
        print("Mathematical operations:")
        print("1.calculate factorial")
        print("2.solve compound interest")
        print("3.Trignomatric calculation")
        print("4.Area of circle")
        print("5.back to main menu")
        c=int(input("Enter your choice:"))
        if c==1:
            n=int(input("enter the number:"))
            print("factorial :",math.factorial(n))
        elif c==2:
            p=float(input("enter principal value:"))
            r=float(input("enter rate(%) value:"))
            t=float(input("enter time value:"))
            amount=p*(1+r/100)**t
            ci=amount - p
            print("compound interest:",ci)
        elif c==3:
            deg=float(input("Enter angle:"))
            rad=math.radians(deg)
            print("sin:",math.sin(rad))
            print("cos:",math.cos(rad))
        elif c==4:
            r=int(input("Enter the radius of circle:"))
            print("area of circle:",math.pi*r*r)
        elif c==5:
            print("back to main menu:")
            break
        else:
            print("Invalid choice, try again.")

def random_oper():
    while True:
        print("Random Data Generation")
        print("1.Random Number")
        print("2.Random List")
        print("3.Random Password")
        print("4.Random OTP")
        print("5.Back to main menu")
        c = int(input("enter your choice:"))
        if c == 1:
                a= int(input("Start: "))
                b= int(input("End: "))
                print("Number:", random.randint(a,b))
        elif c == 2:
                n= int(input("Count: "))
                a=int(input("Start: "))
                b=int(input("End: "))
                print("List:", [random.randint(a,b) for _ in range(n)])
        elif c== 3:
                l = int(input("Length: "))
                chars = string.ascii_letters + string.digits + string.punctuation
                print("Password:", ''.join(random.choice(chars) for _ in range(l)))
        elif c == 4:
            print("OTP:", random.randint(100000,999999))
        elif c==5:
            print("back to main menu:")
            break
        else:
            print("Invalid choice, try again.")
       
def uuid_oper():
    print("generated unique identifiers:")
    print("Generated UUID:", uuid.uuid4())

def explore_modules():
    print("Explore module attribute")
    modules = {"datetime": datetime, "math": math, "random": random, "uuid": uuid, "file_operations": file_operations}
    m = input(f"Enter module name {tuple(modules.keys())}: ").lower().strip()
    print(dir(modules[m]) if m in modules else "Invalid module.")
    input("Press Enter to return...")

def main_menu():
    while True:
        print("Welcome to Multi-Utility Toolkit\n1.Datetime Ops\n2.Math Ops\n3.Random Ops\n4.Generate UUID\n5.File Operations\n6.Explore Modules\n7.Exit")
        c =int(input("enter your choice:"))
        if   c==1: datetime_operation()
        elif c==2: math_operation()
        elif c==3: random_oper()
        elif c==4: uuid_oper()
        elif c==5: file_operations.menu()
        elif c==6: explore_modules()
        else: sys.exit("Thank you for using the Toolkit. 👋")

if __name__ == "__main__":
    try: main_menu()
    except Exception as e: print("Error:", e)        
            
            
        
        
                
            
