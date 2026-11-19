from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [0] * len(nums) 
        postfix = [0] * len(nums)
        output = [0] * len(nums)
        
        for index,value in enumerate(nums):
            if index == 0:
                prefix[index] = 1
            else:
                prefix[index] = prefix[index-1] * nums[index-1]
                
        for i in range (len(nums)-1,-1,-1):
            if i == len(nums) -1:
                postfix[i] = 1
            else:
                postfix[i] = postfix[i+1] * nums[i+1]
                
        for i in range(0,len(nums)):
            output[i] = prefix[i] * postfix[i]
        
        return output