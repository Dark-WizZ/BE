size = int(input("Enter size of the matrix: "))

m1 = [list(map(int, input().split())) for x in range(size)]
res = sum([m1[i][i] for i in range(size)])

print("sum of diagnals: ", res)
