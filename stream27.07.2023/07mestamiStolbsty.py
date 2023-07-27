"""
Дана матрица. Поменять местами две любые ее столбца.
"""

matrix =  [[18, 11,  5,  4, 11],
 [18,  1,  6,  7,  2],
  [2, 14, 14, 10, 12],
 [13,  5, 11, 19, 19],
  [6,  6, 13, 13, 16],
  [0, 17, 14,  6,  0],
 [14,  0,  2, 11,  7]
]

for stroka in matrix:
    print(*stroka)
    
print("Какие столбцы обменять?")
j1 = int(input("Первый столбец: "))-1
j2 = int(input("Вторая столбец: "))-1

for i in range(7):
    #matrix[i][j1], matrix[i][j2] = matrix[i][j2], matrix[i][j1]
    temp = matrix[i][j1]
    matrix[i][j1] = matrix[i][j2]
    matrix[i][j2] = temp
    
for stroka in matrix:
    print(*stroka)