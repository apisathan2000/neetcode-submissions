from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def get_value(item):
            return item[1]

        #frequency Dictionary
        fD = Counter(nums)

        sortedFD = dict(sorted(fD.items() , key=get_value , reverse=True))

        #keys Array - Descending
        kAD = list(sortedFD.keys())

        return kAD[:k]
        