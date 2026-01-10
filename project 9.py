import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class SalesDataAnalyzer:
    def __init__(self):
        self.data = None

    def load_data(self):
        data_path = input("Enter the path of the dataset: ")
        try:
            self.data = pd.read_csv(data_path)
            print("Dataset loaded successfully!")
            return self.data
        except Exception as e:
            print("Error while loading dataset:", e)

    def explore_data(self):
        if self.data is None:
            print("Data is not available, please add dataset")
            return

        print("\n Explore Data")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic information")

        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                print("First 5 rows of dataset:",self.data.head())
            case 2:
                print("Last 5 rows of dataset:",self.data.tail())
            case 3:
                print("Column names of the dataset:",self.data.columns.unique())
            case 4:
                print("Data types of the dataset:",self.data.dtypes)
            case 5:
                print("Basic information of dataset:")
                self.data.info()

            case _:
                print("Invalid choice")

    def dataframe_operation(self):
        if self.data is None:
            print("Data not available.")
            return

        while True:
            print("\n DataFrame Operations ")
            print("1. Add two columns ")
            print("2. Filter data by column value")
            print("3. Delete a column")
            print("4. Go back")

            choice = int(input("Enter choice: "))

            match choice:
                case 1:
                    col1 = input("Enter column 1: ")
                    col2 = input("Enter column 2: ")
                    new_col = input("Enter new column name: ")
                    self.data[new_col] = self.data[col1] + self.data[col2]
                    print(f"{new_col} created successfully!")

                case 2:
                    col = input("Enter column name to filter by: ")
                    value = input("Enter value to filter: ")
                    filtered = self.data[self.data[col] == value]
                    if filtered.empty:
                        print("No matching records found.")
                    else:
                        print("Filtered data:\n", filtered)

                case 3:
                    col = input("Enter the column name to delete: ")
                    if col in self.data.columns:
                        self.data.drop(columns=[col], inplace=True)
                        print(f"Column '{col}' deleted successfully!")
                    else:
                        print(f"Column '{col}' not found in the dataset.")

                case 4:
                    break

                case _:
                    print("Invalid choice")

    def Handle_missing_values(self):
        if self.data is None:
            print("Data is not available, please add dataset")
            return

        while True:
            print("\nHandle Missing Values ")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            print("5. Go back")

            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    rowswithmissingdata = self.data.isna().any(axis=1)
                    df_with_missing = self.data[rowswithmissingdata]
                    if df_with_missing.empty:
                        print("No missing values found in the dataset")
                    else:
                        print("Rows with missing values:\n",df_with_missing)
                        

                case 2:
                    rowswithmissingdata = self.data.isna().any(axis=1)
                    df_with_missing = self.data[rowswithmissingdata]
                    if df_with_missing.empty:
                        print("No missing values found in the dataset")
                    else:
                        mean_values = self.data.mean(numeric_only=True)
                        print(f"Mean of the dataset is:\n{mean_values}")
                        self.data.fillna(mean_values, inplace=True)
                        print("Filling numerical missing values with mean...")
                        print("numerical missing values are filled with mean value")

                case 3:
                    rowswithmissingdata = self.data.isna().any(axis=1)
                    df_with_missing = self.data[rowswithmissingdata]
                    if df_with_missing.empty:
                        print("No missing values found in the dataset")
                    else:
                        print("Dropping rows with missing values...")
                        self.data.dropna(inplace=True)
                        print(self.data)
                        print("Rows with missing values are dropped")
                       

                case 4:
                    rowswithmissingdata = self.data.isna().any(axis=1)
                    df_with_missing = self.data[rowswithmissingdata]
                    if df_with_missing.empty:
                        print("No missing values found in the dataset")
                    else:
                        value = input("Enter the value to replace missing values: ")
                        print("\nReplacing missing values with the provided value...\n")
                        self.data.fillna(value, inplace=True)
                        print(self.data.info())

                case 5:
                    break

                case _:
                    print("Invalid choice")

    def descriptive_statistics(self):
        if self.data is None:
            print("Data not available.")
            return

        while True:
            print(" Data Analysis ")
            print("1. Search specific record")
            print("2. Filter data by condition")
            print("3. Sort data by column")
            print("4. Aggregation functions (sum, mean, max, min)")
            print("5. Descriptive statistics")
            print("6. Go back")

            choice = int(input("Enter choice: "))

            match choice:
                case 1:
                    col = input("Enter column: ")
                    val = input("Enter value: ")
                    print(self.data[self.data[col] == val])

                case 2:
                    col = input("Enter column: ")
                    op = input("Enter operator (=, >, <): ")
                    val = input("Enter value: ")

                    if op == ">":
                        print(self.data[self.data[col] > float(val)])
                    elif op == "<":
                        print(self.data[self.data[col] < float(val)])
                    elif op == "=":
                        print(self.data[self.data[col] == val])
                    else:
                        print("Invalid operator")

                case 3:
                    col = input("Enter column to sort: ")
                    print(self.data.sort_values(by=col))

                case 4:
                    print("Sum:\n", self.data.sum(numeric_only=True))
                    print("Mean:\n", self.data.mean(numeric_only=True))
                    print("Max:\n", self.data.max(numeric_only=True))
                    print("Min:\n", self.data.min(numeric_only=True))

                case 5:
                    print("Descriptive statistics of dataset:\n")
                    print(self.data.describe())
                    print("Standard Deviation:", self.data.std(numeric_only=True))
                    print("Variance:", self.data.var(numeric_only=True))
                    print("Quantile:", self.data.quantile(numeric_only=True))

                case 6:
                    break

                case _:
                    print("Invalid choice")

    def _show_plot(self):
        plt.show()
        input("Press Enter to continue...")
        plt.close()

    def _list_columns(self):
        if self.data is not None:
            cols = ", ".join(str(col) for col in self.data.columns)
            print(f"Available columns: {cols}")

    def _get_column_input(self, prompt, numeric_only=False):
        if self.data is None:
            print("Dataset not loaded.")
            return None

        self._list_columns()
        name = input(prompt).strip()
        if not name:
            print("Column name cannot be empty.")
            return None

        mapping = {str(col).lower(): col for col in self.data.columns}
        column = mapping.get(name.lower())
        if column is None:
            print("Column not found. Please choose from the listed columns.")
            return None

        if numeric_only and not pd.api.types.is_numeric_dtype(self.data[column]):
            print(f"Column '{column}' is not numeric.")
            return None

        return column

    def data_visualization(self):
        if self.data is None:
            print("Data is not available, please add dataset")
            return

        while True:
            print("\nData Visualization ")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            print("7. Go Back")

            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    x_axis = self._get_column_input("Enter x-axis column name: ")
                    y_axis = self._get_column_input("Enter y-axis column name: ", numeric_only=True)
                    if not x_axis or not y_axis:
                        continue
                    print("Generating Bar Plot...")

                    plt.figure(figsize=(10, 5))
                    plt.bar(self.data[x_axis], self.data[y_axis], label=y_axis)
                    plt.title(f"Bar Plot: {y_axis} vs {x_axis}")
                    plt.xlabel(x_axis)
                    plt.ylabel(y_axis)
                    plt.grid(True)
                    plt.legend()
                    plt.tight_layout()
                    self._show_plot()

                case 2:
                    x_axis = self._get_column_input("Enter x-axis column name: ")
                    y_axis = self._get_column_input("Enter y-axis column name: ", numeric_only=True)
                    if not x_axis or not y_axis:
                        continue
                    print("Generating Line Plot...")

                    plt.figure(figsize=(10, 5))
                    plt.plot(self.data[x_axis], self.data[y_axis], label=y_axis)
                    plt.title(f"Line Plot: {y_axis} vs {x_axis}")
                    plt.xlabel(x_axis)
                    plt.ylabel(y_axis)
                    plt.grid(True)
                    plt.legend()
                    plt.tight_layout()
                    self._show_plot()

                case 3:
                    x_axis = self._get_column_input("Enter x-axis column name: ")
                    y_axis = self._get_column_input("Enter y-axis column name: ", numeric_only=True)
                    if not x_axis or not y_axis:
                        continue
                    print("Generating Scatter Plot...")

                    plt.figure(figsize=(10, 5))
                    plt.scatter(self.data[x_axis], self.data[y_axis], label=y_axis)
                    plt.title(f"Scatter Plot: {y_axis} vs {x_axis}")
                    plt.xlabel(x_axis)
                    plt.ylabel(y_axis)
                    plt.grid(True)
                    plt.legend()
                    plt.tight_layout()
                    self._show_plot()

                case 4:
                    col = self._get_column_input("Enter category column (labels): ")
                    val = self._get_column_input("Enter numeric column (values): ", numeric_only=True)
                    if not col or not val:
                        continue

                    print("Generating Pie Chart...")

                    plt.figure(figsize=(8, 8))
                    grouped = self.data.groupby(col)[val].sum()

                    plt.pie(grouped, labels=grouped.index, autopct="%0.2f%%")
                    plt.title(f"Pie Chart: {val} by {col}")
                    plt.legend(title=col)
                    plt.tight_layout()
                    self._show_plot()

                case 5:
                    column = self._get_column_input("Enter column name for histogram: ", numeric_only=True)
                    if not column:
                        continue
                    print("Generating Histogram...")

                    plt.figure(figsize=(10, 5))
                    plt.hist(self.data[column], bins=10, label=column)
                    plt.title(f"Histogram of {column}")
                    plt.xlabel(column)
                    plt.ylabel("Frequency")
                    plt.grid(True)
                    plt.legend()
                    plt.tight_layout()
                    self._show_plot()

                case 6:
                    x_axis = self._get_column_input("Enter x-axis column name: ")
                    y_axis = self._get_column_input("Enter y-axis column name: ", numeric_only=True)
                    if not x_axis or not y_axis:
                        continue

                    print("Generating Stack Plot...")

                    plt.figure(figsize=(10, 5))
                    plt.stackplot(self.data[x_axis], self.data[y_axis], labels=[y_axis])
                    plt.title(f"Stack Plot of {y_axis} over {x_axis}")
                    plt.xlabel(x_axis)
                    plt.ylabel(y_axis)
                    plt.grid(True)
                    plt.legend()
                    plt.tight_layout()
                    self._show_plot()

                case 7:
                    break

                case _:
                    print("Invalid choice")

    def save_visualization_save(self):
        filename = input("Enter filename (e.g., plot.png): ")
        plt.savefig(filename)
        print("Visualization saved successfully!")

    def main(self):
        while True:
            print("\n Data Analysis & Visualization Program")
            print("Please select an option:")
            print("1. Load Dataset")
            print("2. Explore Data")
            print("3. Perform DataFrame Operations")
            print("4. Handle Missing Data")
            print("5. Generate Descriptive Statistics")
            print("6. Data Visualization")
            print("7. Save Visualization")
            print("8. Exit\n")

            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    self.load_data()
                case 2:
                    self.explore_data()
                case 3:
                    self.dataframe_operation()
                case 4:
                    self.Handle_missing_values()
                case 5:
                    self.descriptive_statistics()
                case 6:
                    self.data_visualization()
                case 7:
                    self.save_visualization_save()
                case 8:
                    print("Exiting program. Goodbye!")
                    break
                case _:
                    print("Invalid option! Please try again.")


def main():
    analyzer = SalesDataAnalyzer()
    analyzer.main()


if __name__ == "__main__":
    main()




  






