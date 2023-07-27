'''
Найти сумму элементов матрицы.
'''

spisok = [[ 1,  0,  3,  8,  0],
  [6,  5,  2,  2,  5],
  [5,  6,  4,  2,  3],
  [1,  9,  9,  2,  8]
]

summa = 0

for stroka in spisok:
    for chislo in stroka:
        print(summa, chislo)
        summa = summa + chislo
        
        
print(summa)