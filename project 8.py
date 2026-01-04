import numpy as np

class DataAnalytics:
    def __init__(self):
        self.array = None

    def create_and_index_slice(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            data = list(map(float, input("Enter elements separated by space: ").split()))
            self.array = np.array(data)

        elif choice == 2:
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            total = rows * cols
            data = list(map(float, input(f"Enter {total} elements separated by space: ").split()))
            self.array = np.array(data).reshape(rows, cols)

        elif choice == 3:
            x = int(input("Enter dimension 1: "))
            y = int(input("Enter dimension 2: "))
            z = int(input("Enter dimension 3: "))
            total = x * y * z
            data = list(map(float, input(f"Enter {total} elements separated by space: ").split()))
            self.array = np.array(data).reshape(x, y, z)
        else:
            print("Invalid choice.")
            return

        print("\nArray created successfully:")
        print(self.array)

        while True:
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")

            sub_choice = int(input("Enter your choice: "))

            if sub_choice == 1:
                if self.array.ndim >= 2:
                    i = int(input("Enter row index: "))
                    j = int(input("Enter column index: "))
                    print(f"\nElement at ({i},{j}): {self.array[i, j]}")
                else:
                    i = int(input("Enter index: "))
                    print(f"\nElement at index {i}: {self.array[i]}")

            elif sub_choice == 2:
                if self.array.ndim == 1:
                    start, end = map(int, input("Enter the range (start:end): ").split(":"))
                    print("\nSliced Array:")
                    print(self.array[start:end])
                elif self.array.ndim == 2:
                    r_start, r_end = map(int, input("Enter the row range (start:end): ").split(":"))
                    c_start, c_end = map(int, input("Enter the column range (start:end): ").split(":"))
                    sliced = self.array[r_start:r_end, c_start:c_end]
                    print("\nSliced Array:")
                    print(sliced)
                else:
                    print("\nSlicing for 3D not supported in this simple version.")
            elif sub_choice == 3:
                break
            else:
                print("Invalid choice! Try again.")


    def mathematical_operations(self):
        print("\nMathematical Operations:")
        print("Choose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Enter your choice: "))


        if self.array is None:
            print("No arrays found! Please create an array first.")
            return


        original = self.array
        print(f"\nOriginal Array:\n{original}")


        total = original.size
        data = input(f"\nEnter the same-size array elements ({total} elements separated by space): ").split()
        second = np.array(list(map(float, data))).reshape(original.shape)
        print(f"\nSecond Array:\n{second}")


        if choice == 1:
            result = original + second
            print("\nResult of Addition:")
        elif choice == 2:
            result = original - second
            print("\nResult of Subtraction:")
        elif choice == 3:
            result = original * second
            print("\nResult of Multiplication:")
        elif choice == 4:
            result = original / second
            print("\nResult of Division:")
        else:
            print("Invalid choice!")
            return

        print(result)
        print()

    def combine_or_split_arrays(self):
        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")

        choice = int(input("Enter your choice: "))


        if self.array is None:
            print("No arrays found! Please create an array first.")
            return

        original = self.array

        if choice == 1:

            print("\nOriginal Array:")
            print(original)

            total = original.size
            shape = original.shape
            rows, cols = shape


            data = input(f"\nEnter the elements of another array to combine ({total} elements separated by space): ").split()
            new_arr = np.array(list(map(float, data))).reshape(rows, cols)

            print("\nSecond Array:")
            print(new_arr)


            combined = np.vstack((original, new_arr))

            print("\nCombined Array (Vertical stack):")
            print(combined)

        elif choice == 2:

            print("\nOriginal Array:")
            print(original)

            parts = int(input("Enter the number of parts to split the array into: "))
            try:
                split_arrays = np.array_split(original, parts)
                for i, part in enumerate(split_arrays, start=1):
                    print(f"\nPart {i}:")
                    print(part)
            except Exception as e:
                print("Error:", e)

        else:
            print("Invalid choice!")
    def search_sort_filter(self):
        print("\nSearch, Sort, and Filter:")
        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")

        choice = int(input("\nEnter your choice: "))

        if self.array is None:
            print("Array not created!")
            return

        arr = self.array
        print("\nOriginal Array:")
        print(arr)

        if choice == 1:

            val = float(input("\nEnter value to search: "))
            result = np.where(arr == val)
            if result[0].size > 0:
                print(f"\nValue {val} found at positions: {list(zip(result[0], result[1]))}")
            else:
                print(f"\nValue {val} not found in the array.")

        elif choice == 2:

            sorted_arr = np.sort(arr, axis=1)
            print("\nSorted Array:")
            print(sorted_arr)
            print("\n(Sorting applied row-wise.)")

        elif choice == 3:

            threshold = float(input("\nEnter value to filter greater than: "))
            filtered = arr[arr > threshold]
            print(f"\nValues greater than {threshold}: {filtered}")

        else:
            print("\nInvalid choice!")

    def aggregates_and_statistics(self):
        print("\nAggregates and Statistics:")
        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")

        choice = int(input("\nEnter your choice: "))


        if self.array is None:
            print("Array not created!")
            return

        arr = self.array
        print("\nOriginal Array:")
        print(arr)


        if choice == 1:
            result = np.sum(arr)
            print(f"\nSum of Array: {result}")

        elif choice == 2:
            result = np.mean(arr)
            print(f"\nMean of Array: {result}")

        elif choice == 3:
            result = np.median(arr)
            print(f"\nMedian of Array: {result}")

        elif choice == 4:
            result = np.std(arr)
            print(f"\nStandard Deviation of Array: {result}")

        elif choice == 5:
            result = np.var(arr)
            print(f"\nVariance of Array: {result}")

        else:
            print("\nInvalid choice!")
    def menu(self):
        print("\nWelcome to the NumPy Analyzer!")
        while True:
            print("\n NumPy Analyzer")
            print("1. Create Array + Index/Slice")
            print("2. Mathematical Operations")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, and Filter")
            print("5. Aggregates and Statistics")
            print("6. Exit")

            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                self.create_and_index_slice()
            elif choice == 2:
                self.mathematical_operations()
            elif choice == 3:
                self.combine_or_split_arrays()
            elif choice == 4:
                self.search_sort_filter()
            elif choice == 5:
                self.aggregates_and_statistics()
            elif choice == 6:
                print("Thank you for using Numpy Analyzer, GoodBye!")
                break
            else:
                print("Invalid choice! Try again.")

da=DataAnalytics()
da.menu()
