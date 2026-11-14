from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramDict :dict[tuple, List[str]]  = {}
        
        for x in strs:
            key = tuple(sorted(Counter(x).items()))
            
            if key in anagramDict:
                anagramDict[key].append(x)
            
            else:
                anagramDict[key] = [x]
            
        
        return list(anagramDict.values())