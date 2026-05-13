from typing import List
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        groupedList = []
        for x in strs:
            key = "".join(sorted(x))
            if key in anagrams:
                anagrams[key].append(x)
            else:
                anagrams[key] = [x]

        return list(anagrams.values())
