#-------------------------------------------------------------------------------
# Name:        Project_Euler_problem_2
# Purpose:
#
# Author:      phuang
#
# Created:     26/05/2016
# Copyright:   (c) phuang 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    sum = 2
    xi = 3 * 2 + 2 * 1
    prexi = 2 * 2 + 1

    while (xi < 4000000):
        sum += xi
        temp = 3 * xi + 2 * prexi
        prexi = 2 * xi + prexi
        xi = temp
    print(sum)

if __name__ == '__main__':
    main()
