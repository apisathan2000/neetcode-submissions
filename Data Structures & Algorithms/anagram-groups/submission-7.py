from collections import Counter
 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counterDict : dict[tuple,  List[str]] = {}
        finalArray = []

        for index,x in enumerate(strs):
            counterX = Counter(x)
            keyX = tuple(sorted(counterX.items()))
            if keyX in counterDict:
                counterDict[keyX].append(x)
            else:
                counterDict[keyX] = [x]

        return list(counterDict.values());
            
            

        