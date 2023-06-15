'''
#######
#######
*******
#######
#######
#######
*******
#######
#######

'''

for row in range(1, 10):
    for column in range(1, 8):
        if row % 4 == 3:
            print('*', end="")
        else:
            print('#', end="")
    print()