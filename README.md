Sparse Matrix Operator
Programming Assignment 2: Sparse Matrix
Task Description:
Using any programming language of your choice.

Load two sparse matrices from an input file.
Perform addition, subtraction, and multiplication on the matrices.
Features
Loads two sparse matrices from an input file performs addition performs subtraction performs multiplication

Requirements
Python compiler (interpreter): depending on your machine specifications python or python3 is required for this program. Use python --version to check the version of python on your machine.

How to Use
Installation
You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.

git clone https://github.com/Hirw23/dsa.git
After cloning the repo, navigate using the absolute path: dsa/hw02/code/src/ using this as the argument to the cd command, in the src directory lies the program.

This is still a demo, so all input files that are to be handled by the program must be in the same directory as the program source file, which is the src directory.

To compile and run the program run the following command in your terminal: python(3) -u <program_file-name> <input_file-name> <input_file02-name> The python interpreter you use is dependent on the version installed on your machine; for me this will look like this: python3 -u [SparseMatrix.py] [easy_sample_01_1.txt] [easy_sample_01_2.txt]

Pls note that square brackets won't be used when actually running the program, this has been included for emphatic basis.

<input_file-name> - file containing matrix

Example
Say we have an input file easy_sample_input_02.txt with the following content:

rows=1 cols=2 (0, 1, 3) (0, 2, 4)

and another file easy_sample_input_03.txt with the following content:

rows=1 cols=2 (0, 1, 5) (0, 2, 10)

run the program: python(3) -u SparseMatrix.py easy_sample_input_02.txt easy_sample_input_03.txt

Output
addition rows=1 cols=2 (0, 1, 8) (0, 2, 14)

subtraction rows=1 cols=2 (0, 1, -2) (0, 1, -6)

multiplication In this case multiplication is not feasible as the value for cols for the first matrix is not equal to the value for rows in the second matrix.

Three separate files indicating addition, subtraction, and multiplication: addition.txt subtraction.txt multiplication.txt

Handling Different Input Scenarios
Whitespace Handling:
Lines with only whitespace characters are skipped Leading and trailing whitespaces around integers are ignored.

Empty Lines:
Lines that are completely empty or contain only whitespace are skipped.

Author
Hirwa Walid w.hirwa@alustudent.com