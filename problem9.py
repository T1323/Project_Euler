#-------------------------------------------------------------------------------
# Name:        project euler  problem9
# Purpose:
#
# Author:      phuang
#
# Created:     30/05/2016
# Copyright:   (c) phuang 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    find = False
    for x in range(1,500):
        if find:
            break
        for y in range(x, 500):
            if find:
                break
            for z in range(y, x + y):
                if (x + y + z == 1000) and (x*x + y*y == z*z):
                    print([x, y, z])
                    print(x*y*z)
                    find = True
                    break
    if find == False:
        print("fail")


if __name__ == '__main__':
    main()
