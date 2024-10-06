import os


class SparseMatrix:
    def __init__(self, matrixFilePath=None, numRows=None, numCols=None):
        if matrixFilePath:
            self.numRows, self.numCols, self.elements = self.read_matrix_file(matrixFilePath)
        else:
            self.numRows = numRows
            self.numCols = numCols
            self.elements = {}

    @staticmethod
    def read_matrix_file(filePath):
        elements = {}
        with open(filePath, 'r') as file:
            lines = file.readlines()
            numRows = int(lines[0].split('=')[1])
            numCols = int(lines[1].split('=')[1])
            for line in lines[2:]:
                line = line.strip()
                if not line:
                    continue
                if line.startswith('(') and line.endswith(')'):
                    row, col, value = map(int, line[1:-1].split(','))
                    if row not in elements:
                        elements[row] = {}
                    elements[row][col] = value
                else:
                    raise ValueError("Input file has wrong format")
        return numRows, numCols, elements

    def getElement(self, currRow, currCol):
        return self.elements.get(currRow, {}).get(currCol, 0)

    def setElement(self, currRow, currCol, value):
        if currRow not in self.elements:
            self.elements[currRow] = {}
        self.elements[currRow][currCol] = value

    def add(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrices dimensions do not match for addition")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for row in range(self.numRows):
            for col in range(self.numCols):
                sum_value = self.getElement(row, col) + other.getElement(row, col)
                if sum_value != 0:
                    result.setElement(row, col, sum_value)
        return result

    def subtract(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrices dimensions do not match for subtraction")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for row in range(self.numRows):
            for col in range(self.numCols):
                diff_value = self.getElement(row, col) - other.getElement(row, col)
                if diff_value != 0:
                    result.setElement(row, col, diff_value)
        return result

    def multiply(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrices dimensions do not match for multiplication")
        result = SparseMatrix(numRows=self.numRows, numCols=other.numCols)
        for i in range(self.numRows):
            for j in range(other.numCols):
                sum_value = 0
                for k in range(self.numCols):
                    sum_value += self.getElement(i, k) * other.getElement(k, j)
                if sum_value != 0:
                    result.setElement(i, j, sum_value)
        return result

    def __str__(self):
        result = []
        for row in range(self.numRows):
            for col in self.elements.get(row, {}):
                result.append(f"({row}, {col}, {self.elements[row][col]})")
        return '\n'.join(result)


def write_matrix_to_file(matrix, filePath):
    os.makedirs(os.path.dirname(filePath), exist_ok=True)
    with open(filePath, 'w') as file:
        file.write(f"rows={matrix.numRows}\n")
        file.write(f"cols={matrix.numCols}\n")
        file.write(str(matrix))


def get_valid_operation():
    while True:
        print("Select the operation you want to perform:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        operation = input("Enter the number corresponding to the operation: ").strip()
        if operation in {"1", "2", "3"}:
            return operation
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")


def main():
    while True:
        # Input file paths from user
        file1 = input("Please enter the path to the first matrix file: ").strip(r'C:\Users\Hp\PycharmProjects\dsa\sparse_matrix\sample_inputs')   # Absolute path to matrix 1
        file2 = input("Please enter the path to the second matrix file: ").strip(r'C:\Users\Hp\PycharmProjects\dsa\sparse_matrix\sample_inputs')  # Absolute path to matrix 2
        # You can change the paths above to the correct file locations


        try:
            # Read matrices from files
            matrix1 = SparseMatrix(matrixFilePath=file1)
            matrix2 = SparseMatrix(matrixFilePath=file2)

            print(f"Matrix 1: {matrix1.numRows}x{matrix1.numCols}")
            print(f"Matrix 2: {matrix2.numRows}x{matrix2.numCols}")

            # Get valid operation from user
            operation = get_valid_operation()

            # Define output file paths
            base_output_path = r'C:\Users\Hp\PycharmProjects\dsa\\sample_results\\'
            addition_file = os.path.join(base_output_path, "Addition_result.txt")
            subtraction_file = os.path.join(base_output_path, "Subtraction_result.txt")
            multiplication_file = os.path.join(base_output_path, "Multiplication_result.txt")

            # Perform the selected operation
            if operation == "1":  # Addition
                if matrix1.numRows == matrix2.numRows and matrix1.numCols == matrix2.numCols:
                    result = matrix1.add(matrix2)
                    write_matrix_to_file(result, addition_file)
                    print(f"Addition result has been written to {addition_file}")
                else:
                    print("Addition skipped due to dimension mismatch")
            elif operation == "2":  # Subtraction
                if matrix1.numRows == matrix2.numRows and matrix1.numCols == matrix2.numCols:
                    result = matrix1.subtract(matrix2)
                    write_matrix_to_file(result, subtraction_file)
                    print(f"Subtraction result has been written to {subtraction_file}")
                else:
                    print("Subtraction skipped due to dimension mismatch")
            elif operation == "3":  # Multiplication
                if matrix1.numCols == matrix2.numRows:
                    result = matrix1.multiply(matrix2)
                    write_matrix_to_file(result, multiplication_file)
                    print(f"Multiplication result has been written to {multiplication_file}")
                else:
                    print("Multiplication skipped due to dimension mismatch")
        except FileNotFoundError:
            print(f"Error: One or both files could not be found. Please check the file paths and try again.")
        except ValueError as e:
            print(f"Error: {e}")

        # Ask the user if they want to perform another operation
        if input("Do you want to perform another operation? (yes/no): ").strip().lower() != 'yes':
            break


if __name__ == '__main__':
    main()
