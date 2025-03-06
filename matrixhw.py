
A = [[1, 2], [2, 1]]
B = []
for i in range(2):
    temp = []
    for j in range(2):
        temp.append(int(input(f"Please enter the value of matrix B at position ({i},{j}): ")))
    B.append(temp)


print("Matrix A:")
for row in A:
    print(row)

print("Matrix B:")
for row in B:
    print(row)

C = [[0, 0], [0, 0]]

for i in range(2): 
    for j in range(2): 
        C[i][j] = A[i][j] - B[i][j]

print("Matrix C (A - B):")
for row in C:
    print(row)

