[m, n] = list(map(int, input("Enter size of the matrix(row,column): ").split()))
print("Enter values for matrix 1: ")
m1 = [list(map(int, input().split())) for x in range(m)]
print("Enter values for matrix 2: ")
m2 = [list(map(int, input().split())) for x in range(m)]
res = [[m1[i][j] + m2[i][j] for j in range(n)] for i in range(m)]
res = [[a + b for a, b in zip(i, j)] for i, j in zip(m1, m2)]
print("Matrix 1: ", m1)
print("Matrix 2: ", m2)
print("Result matrix: ", res)
