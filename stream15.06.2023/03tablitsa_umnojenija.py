"""
Выведите таблицу умножения от 1 до 9

1  2  3  4  5  6  7  8  9
2  4  6  8  10  12  14 16 18
3  6  9  12  15  18  21  24  27
...
"""

for row in range(1,10):
    for column in range(1,10):
        print(row*column, end='  ')
    print()


