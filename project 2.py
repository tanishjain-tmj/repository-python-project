print("Welcome to Pattern Generator and Number Analyzer")

while True:
    if False:
        pass
    else:
    
        print("Select an Option:")
        print("1.Generate a Pattern")
        print("2.Analze a range of Numbers")
        print("3.Exit")

        choice=int(input("Enter your choice:"))
        print()
        match choice:
            case 1:
                r=int(input("Enter the number of rows:"))
                for i in range(1,r+1):
                    for j in range(1,i+1):
                        print("*",end=" ")
                    print()
            case 2:
                start=int(input("Enter the start of the Range:"))
                end=int(input("Enter the end of the Range:"))
                total=0
                for i in range(start,end+1):
                    if i%2==0:
                        print("Number",i,"is Even.")
                    else:
                        print("Number",i,"is Odd")
                    total=total+i
                print("Total Addition=",total)
            case 3:
                print("Exit program")
                break
