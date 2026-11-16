from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #frequenct Dictionary
        fD = Counter(nums)

        #sorted Frequency Dictionary 
        sortedFd = dict(sorted(fD.items() , key = lambda item:item[1] , reverse=True))

        #final Array
        sortedArray = list(sortedFd.keys())

        return sortedArray[:k]
        