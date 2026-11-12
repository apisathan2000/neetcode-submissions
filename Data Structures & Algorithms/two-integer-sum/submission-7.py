from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for index, value in enumerate(nums):
            difference = target - value
            if difference in dict:
                unsorted = [dict[difference], index]
                unsorted.sort()
                sorted = unsorted.copy()
                return sorted

            else: 
                dict[value] = index