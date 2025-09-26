data = []

while True:
    print("Welcome to the data Analyze and Transformer program")
    print("")
    print("Main Menu:")
    print("")
    print("1. Input data")
    print("2. Display data summary")
    print("3. Calculate factorial")
    print("4. Filter data by Threshold")
    print("5. Sort data")
    print("6. Display dataset Statistics")
    print("7. Exit program")
    print("")

    choice = int(input("Please enter your choice: "))

    match choice:
        case 1:
            arr = input("Enter data for 1D array (separated by space): ")
            data = [int(x) for x in arr.split()]
            print("")
            print("Data has been stored successfully")
            print(data)

        case 2:
            print("Data summary:")
            count = 0
            for i in data:
                count += 1
            print("Total elements:", count)
            print("Minimum element:", min(data))
            print("Maximum element:", max(data))
            print("Sum of all values:", sum(data))
            average = sum(data) / count
            print("Average:", average)

        case 3:
            n = int(input("Enter a number to calculate factorial: "))

            def factorial(n):
                if n < 0:
                    return "Factorial is not defined for negative numbers"
                elif n == 0 or n == 1:
                    return 1
                else:
                    return n * factorial(n - 1)

            print(f"Factorial of {n}: {factorial(n)}")

        case 4:
            n = int(input("Enter a threshold value to filter out data above this value: "))
            n_new = list(filter(lambda x: x >= n, data))
            print(f"Filtered data (values >= {n}):", n_new)

        case 5:
            print("Choose sorting option:")
            print("1. Ascending")
            print("2. Descending")
            sort = int(input("Enter your choice: "))
            if sort == 1:
                data.sort()
                print("Sorted data:", data)
            elif sort == 2:
                data.sort(reverse=True)
                print("Sorted data:", data)
            else:
                print("Invalid sort option.")

        case 6:
            print("Dataset Statistics:")
            count = 0
            for i in data:
                count += 1
            print("- Minimum element:", min(data))
            print("- Maximum element:", max(data))
            print("- Sum of all values:", sum(data))
            average = sum(data) / count
            print("- Average:", average)

        case 7:
            print("Thank you for using the Data Analyzer and Transformer program. Goodbye!")
            break  # Needed to exit the loop

        case _:
            print("Invalid choice. Please select a valid option.")


    
    
