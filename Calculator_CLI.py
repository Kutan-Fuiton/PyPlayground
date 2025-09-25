# Simple Calculator CLI
import numpy as np
import re
import math

# basic arithmetic operations: addition, subtraction, multiplication, and division.
def add(a,b): return a + b
def subtract(a,b): return a - b
def multiply(a,b): return a * b
def divide(a,b): return a / b if b != 0 else 'Indeterminate Form: Division by Zero (Finite / 0)'

# Advanced operations: exponentiation and square root.
def power(a,b): return a ** b if not (a == 0 and b <= 0) else 'Indeterminate Form: 0 raised to Negative Power (0 ** -n or 0 ** 0)'
def square_root(a): return a ** 0.5 if a >= 0 else 'Not Possible [Complex Number]: Square Root of Negative Number (sqrt(negative)'

# Matrix operations: addition, subtraction, multiplication, and transpose using numpy
def get_matrix():    # Matrix Input Function
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Enter the matrix row by row, with elements separated by spaces:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").strip().split()))
        if len(row) != cols:
            raise ValueError("Number of elements in the row does not match the specified number of columns.")
        matrix.append(row)
    return np.array(matrix)
def matrix_add(A, B):     # Matrix Addition Function
    try: 
        return np.add(A, B)
    except ValueError:
        return 'Error: Matrices must have the same dimensions for addition.'
def matrix_subtract(A, B):     # Matrix Subtraction Function
    try:
        return np.subtract(A, B)
    except ValueError:
        return 'Error: Matrices must have the same dimensions for subtraction.'
def matrix_multiply(A, B):     # Matrix Multiplication Function
    try:
        return A @ B
    except ValueError:
        return 'Error: Number of columns in the first matrix must equal the number of rows in the second matrix for multiplication.'
def matrix_transpose(A): return np.transpose(A)     # Matrix Transpose Function


def normalize(expr: str) -> str:
    expr = expr.lower().strip()
    # Add spaces around operators
    expr = re.sub(r'([+\-*/^x])', r' \1 ', expr)
    expr = re.sub(r'\s+', ' ', expr).strip()  # remove extra spaces
    return expr

safe_env = {
    "sqrt": math.sqrt,
    "pow": pow,
    "__builtins__": {}
}


def main():
    print("Welcome to the Simple Calculator CLI with BODMAS support!")
    print("Examples:")
    print(" - 3+4*2, (5+7)/2, 2^3+4, sqrt25+3")
    print(" - Matrix: matrix add, matrix subtract, matrix multiply, matrix transpose\n")

    while True:
        user_input = input("Calculate (or type 'exit'): ").strip().lower()
        if user_input == 'exit':
            print("Goodbye! 👋")
            break

        # ---------------- Matrix Operations ----------------
        if user_input.startswith("matrix"):
            try:
                if "add" in user_input:
                    A = get_matrix("Matrix A"); B = get_matrix("Matrix B")
                    print("Result:\n", matrix_add(A, B))
                elif "subtract" in user_input:
                    A = get_matrix("Matrix A"); B = get_matrix("Matrix B")
                    print("Result:\n", matrix_subtract(A, B))
                elif "multiply" in user_input:
                    A = get_matrix("Matrix A"); B = get_matrix("Matrix B")
                    print("Result:\n", matrix_multiply(A, B))
                elif "transpose" in user_input:
                    A = get_matrix("Matrix A")
                    print("Result:\n", matrix_transpose(A))
                else:
                    print("Unknown matrix operation. Try: matrix add | subtract | multiply | transpose")
            except Exception as e:
                print("Error:", e)
            continue

        # ---------------- Regular Arithmetic with BODMAS ----------------
        try:
            expr = normalize(user_input)
            result = eval(expr, safe_env)
            print("Result:", result)
        except Exception as e:
            print("Error in expression:", e)


if __name__ == "__main__":
    main()