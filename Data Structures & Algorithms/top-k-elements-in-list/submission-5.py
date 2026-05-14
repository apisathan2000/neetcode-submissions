from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        kfrequent = []

        for x in nums:
            if x in counter:
                counter[x] += 1
            else:
                counter[x] = 1

        sorted_dict = dict(
            sorted(counter.items(), key=lambda item: item[1], reverse=True)
        )

        kfrequent = list(sorted_dict.keys())[:k]

        return kfrequent

