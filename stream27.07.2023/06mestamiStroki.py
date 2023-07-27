"""
Дана матрица. Поменять местами две любые ее строки.
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
print("Какие строки обменять?")
i1 = int(input("Первая строка: "))-1
i2 = int(input("Вторая строка: "))-1


temp = matrix[i1]
matrix[i1] = matrix [i2]
matrix[i2] = temp
#или
#matrix[i1], matrix[i2] = matrix[i2], matrix[i1]

for stroka in matrix:
    print(*stroka)