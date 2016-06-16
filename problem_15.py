#-------------------------------------------------------------------------------
# Name:        project euler problem15
# Purpose:
#
# Author:      phuang
#
# Created:     15/06/2016
# Copyright:   (c) phuang 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def latticePaths(row, col):
    if row == 0 or col == 0:
        return 1
    else:
        return latticePaths(row - 1, col) + latticePaths(row, col - 1)

def latticePaths2(row, col):
    grid = [[0 for i in range(row + 1)] for j in range(row + col + 1)]
    grid[0][0] = 1

    for i in range(1, row + col + 1):
        if i <= (row + col) // 2:
            for j in range(0, i + 1):
                left = 0
                right = 0
                if j > 0:
                    left = grid[i-1][j-1]
                if j < i:
                    right = grid[i-1][j]
                grid[i][j] = left + right
        else:
            for j in range(0, row + col - i + 1):
                left = grid[i-1][j]
                right = grid[i-1][j+1]
                grid[i][j] = left + right

    return grid[row + col][0]




if __name__ == '__main__':
    answer = latticePaths2(20, 20)
    print(answer)
