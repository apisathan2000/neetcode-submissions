from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        hDict = dict()
        vDict = dict()
        x3Dict = dict()

        for x in board:
            for y in x:
                if y in hDict:
                    hDict[y] += 1
                else:
                    hDict[y] = 1

            hDict.pop("." , None)

            # print(hDict)

            for z in hDict:
                if hDict[z] != 1:
                    print("False")
                    return False

            hDict.clear()

        transposed = list(map(list, zip(*board)))

        for x in transposed:
            for y in x:
                if y in vDict:
                    vDict[y] += 1
                else:
                    vDict[y] = 1

            vDict.pop("." , None)

            # print(vDict)

            for z in vDict:
                if vDict[z] != 1:
                    print("False")
                    return False

            vDict.clear()

        arrayNum = 0
        lastArray = 0

        res: List[List[str]] = [[], [], [], [], [], [], [], [], []]
        

        for i, x in enumerate(board):

            for index, value in enumerate(x):
                if index % 3 == 0 and index > 0:
                    arrayNum = arrayNum + 1
                res[arrayNum].append(value)

            lastArray = arrayNum

            if (i + 1) % 3 != 0:
                arrayNum = lastArray - 2
            else:
                arrayNum = arrayNum + 1

        for x in res:
            print(x)
            
        for x in res:
            for y in x:
                if y in x3Dict:
                    x3Dict[y] += 1
                else:
                    x3Dict[y] = 1

            x3Dict.pop("." , None)

            # print(vDict)

            for z in x3Dict:
                if x3Dict[z] != 1:
                    print("False")
                    return False

            x3Dict.clear()
        print("True")
        return True
