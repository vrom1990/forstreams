"""
*****
*****
****#
***#*
**#**
"""

for row in range(1, 5):
    for column in range(1, 5):
        if row + column == 6:
            print('#', end="")
        else:
            print('*', end="")
    print()