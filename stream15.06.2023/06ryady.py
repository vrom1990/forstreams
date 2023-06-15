'''
*#*#*#
*#*#*#
*#*#*#
*#*#*#
*#*#*#
*#*#*#

'''


for row in range(1, 7):
    for column in range(1, 7):
        if column % 2 == 0:
            print('#', end="")
        else:
            print('*', end="")
    print()