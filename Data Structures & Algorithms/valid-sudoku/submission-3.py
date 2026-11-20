from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        fqDict = {}
        transposed = [["." for _ in range(0, 9)] for _ in range(0, 9)]
        square = [["." for _ in range(0, 9)] for _ in range(0, 9)]
        colValid = True
        rowValid = True
        sqValid = True

        for x in board:
            fqDict = {}
            for y in x:
                if y == ".":
                    continue
                elif y in fqDict:
                    rowValid = False
                    break
                else:
                    fqDict[y] = 1

        for i in range(0, 9):
            for j in range(0, 9):
                transposed[j][i] = board[i][j]

        for x in transposed:
            fqDict = {}
            for y in x:
                if y == ".":
                    continue
                elif y in fqDict:
                    colValid = False
                    break
                else:
                    fqDict[y] = 1

        fqDict = {}
        arrayIndextoStore = 0
        itemIndextoStore = 0

        for i in range(0, 9):

            if i != 0 and i % 3 == 0:
                arrayIndextoStore += 1
                itemIndextoStore = 0

            else:
                if i != 0:
                    arrayIndextoStore -= 2
                    itemIndextoStore += 1

            for j in range(0, 9):

                if j != 0 and j % 3 == 0:
                    arrayIndextoStore += 1
                    itemIndextoStore -= 2

                else:
                    if j != 0:
                        itemIndextoStore += 1

                square[arrayIndextoStore][itemIndextoStore] = board[i][j]

        for x in square:
            fqDict = {}
            for y in x:
                if y == ".":
                    continue
                elif y in fqDict:
                    sqValid = False
                    break
                else:
                    fqDict[y] = 1

        return colValid and rowValid and sqValid
