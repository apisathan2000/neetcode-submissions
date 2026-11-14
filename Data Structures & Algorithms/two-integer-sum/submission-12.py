from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}


        for index,value in enumerate(nums):
            difference = target - value
           
            if value in dict:
                return sorted([index, dict[value]])

            dict[difference] = index

            


         
            