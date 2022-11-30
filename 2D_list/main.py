matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])
print("\n")

for row in matrix:
    for item in row:
        print(item)

print('\n')
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j])