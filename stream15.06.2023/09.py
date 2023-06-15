"""
3 6 9 12
4 7 10 13
5 8 11 14
6 9 12 15
"""

for row in range(1, 5):
    for column in range(1, 5):
        print(column*3+row-1, end=" ")
    print()

