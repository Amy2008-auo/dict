A=[[1,2],[2,1]]
B=[]
for i in range(2):
    temp=[]
    for j in range(2):
        temp.append(int(input("Please enter the value of matrix B")))
    B.append(temp)
print(A)
print(B)
C=[[0,0],[0,0]]
for i in range(2): #row
    for j in range(2):#colon
        C[i][j]=A[i][j]+B[i][j]

print(C)