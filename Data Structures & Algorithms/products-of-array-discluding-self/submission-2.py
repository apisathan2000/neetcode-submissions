from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        
        
        for x in range(0,len(nums)):
            product = 1
            
  
            for y in range(0, len(nums)):
                if x == y :
                    continue
                product = product * nums[y]
                
            res.append(product)

       

        print(res)
        return res