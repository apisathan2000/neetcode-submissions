from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #frequency Dictionary
        fD = Counter(nums)

        sortedFD = dict(sorted(fD.items() , key=lambda item:item[1] , reverse=True))

        #keys Array - Descending
        return list(sortedFD.keys())[:k]
        