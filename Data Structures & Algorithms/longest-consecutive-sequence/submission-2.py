from typing import List
from collections import Counter


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        fqDict = Counter(nums)
        consecutiveArray = []
        arrayList = []

        sortedList = sorted(fqDict.keys())

        print(sortedList)

        for i in range(0, len(sortedList)):
            if i == 0:
                consecutiveArray.append(sortedList[i])
                if i == len(sortedList) - 1:
                    arrayList.append(consecutiveArray)
            else:
                length = len(consecutiveArray)
                lastIndex = length - 1
                if sortedList[i] == consecutiveArray[lastIndex] + 1:

                    consecutiveArray.append(sortedList[i])
                    if i == len(sortedList) - 1:
                        arrayList.append(consecutiveArray)
                else:
                    arrayList.append(consecutiveArray)
                    consecutiveArray = []
                    consecutiveArray.append(sortedList[i])

        max = 1

        if len(arrayList) == 0:
            max = 0
        else:
            for x in arrayList:
                if len(x) > max:
                    max = len(x)

        return max