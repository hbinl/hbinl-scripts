__author__ = 'HaoBin'


def matrix_print(m):
    for i in range(len(m)):
        print(m[i])

def matrix_get(m_row, m_column):
    m = []
    for i in range(m_row):
        x = input("Row " + str(i+1) + ": ")
        x = [int(n) for n in x.split()]
        if len(x) < m_column:
            for j in range(m_column - len(x)):
                x.append(0)
        m.append(x[0:m_column])

    return m

def matrix_multiply(row, column, m1, m2):
    m3 = []

    for i in range(row):
        tmp = []
        for j in range(column):
            x = 0
            for k in range(len(m2)):
                x += m1[i][k] * m2[k][j]
            tmp.append(x)
        m3.append(tmp)

    return m3

def matrix_input():
    m1_row = int(input("Matrix 1, number of rows: "))
    m1_column = int(input("Matrix 1, number of columns: "))

    m2_row = int(input("Matrix 2, number of rows: "))
    m2_column = int(input("Matrix 2, number of columns: "))

    if m1_column != m2_row:
        print("M1 columns must be equal to M2 rows to perform matrix multiplication.")
    else:
        print("This will result in a " + str(m1_row) + "x" + str(m2_column) + " matrix.")
        print("Please enter your matrix 1, with each number separated by space. Excess numbers will be trimmed.")
        m1 = matrix_get(m1_row, m1_column)

        print("Please enter your matrix 2, with each number separated by space. Excess numbers will be trimmed.")
        m2 = matrix_get(m2_row, m2_column)

        print("-"*20)
        matrix_print(m1)
        print("*")
        matrix_print(m2)
        print("=")
        m3 = matrix_multiply(m1_row, m2_column, m1, m2)
        matrix_print(m3)


if __name__ == "__main__":
    try:
        matrix_input()

    except ValueError:
        print("Invalid number input.")