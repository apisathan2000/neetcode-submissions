from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        cumulativePrefix, cumulativeSuffix , res = [], [] , []

        prefixProduct = 1
        suffixProduct = 1
        for x in range(0, len(nums)):
            if x == 0 :
                prefixProduct = 1
            else: 
                prefixProduct *= nums[x-1]
            cumulativePrefix.append(prefixProduct)

        
        for x in range(len(nums)-1, -1, -1):
            if x == len(nums)-1:
                suffixProduct = 1
            else:
                suffixProduct *= nums[x+1]
            cumulativeSuffix.append(suffixProduct)
            
        cumulativeSuffix.reverse()

        # print(cumulativePrefix)
        # print(nums)
        # print(cumulativeSuffix)
        
        
        for x in range(0, len(nums)): 
            product = cumulativePrefix[x] * cumulativeSuffix[x]
            res.append(product)
        
        print(res)
        return res
