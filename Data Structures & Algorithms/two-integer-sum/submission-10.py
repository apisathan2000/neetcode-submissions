from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}


        for index,value in enumerate(nums):
            difference = target - value
           
            if value in dict:
                finalArray = sorted([index, dict[value]])
                return finalArray

            dict[difference] = index
        
        
            

        
        




           

        return [0,2]

            


         
            