#-------------------------------------------------------------------------------
# Name:        Project_Euler  Problem1
# Purpose:
#
# Author:      phuang
#
# Created:     26/05/2016
# Copyright:   (c) phuang 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    sum = 0
    elements = [i for i in range(1000) if (i % 3 == 0 or i % 5 == 0)]
    for element in elements:
        sum = sum + element
    print(sum)

if __name__ == '__main__':
    main()
