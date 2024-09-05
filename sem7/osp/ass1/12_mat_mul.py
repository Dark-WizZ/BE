[m, n] = list(map(int, input("Enter size of the matrix(row,column): ").split()))
p = int(input("Enter size of the matrix(column): "))
print("Enter values for matrix 1: ")
m1 = [list(map(int, input().split())) for x in range(m)]
print("Enter values for matrix 2: ")
m2 = [list(map(int, input().split())) for x in range(n)]
res = [[sum(i * j for i, j in zip(row, col)) for col in zip(*m2)] for row in m1]
print("Matrix 1: ", m1)
print("Matrix 2: ", m2)
print("Result matrix: ", res)
