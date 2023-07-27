'''
В двумерном массиве (матрице)
найти индексы (номера строк и столбцов) максимальных элементов.
'''

matrix =  [[-24,  -1, -14,  -1,  16, -13,  23],
 [-24,  -9, -22, -25,  -4,   8, -16],
 [-15,  -6, -3,  18,   3,   7, -24],
 [10,   6, -22,  17,   3,  -4,  23],
 [-3, -17,  -4,  -6,   4,  18,  -7]
]

max = matrix[0][0]
stroki= []
strolbtsy = []

for i in range(5):
    for j in range(7):
        
        if matrix[i][j] > max:
            max = matrix[i][j]
print(max)

for i in range(5):
    for j in range(7):
        if matrix[i][j] == max:
            stroki.append(i+1)
            strolbtsy.append(j+1)

for i in range(len(stroki)):
    print(stroki[i], strolbtsy[i])