from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        cumulativePrefix = [1] * n
        cumulativeSuffix = [0] * n
        res = [0] * len(nums)

        cumulativeSuffix[n - 1] = cumulativePrefix[0] = 1

        for i in range(1, n):
            cumulativePrefix[i] = cumulativePrefix[i - 1] * nums[i - 1]

        for i in range(n-2, -1, -1):
            cumulativeSuffix[i] = cumulativeSuffix[i + 1] * nums[i + 1]

        for i in range(n):
            res[i] = cumulativePrefix[i] * cumulativeSuffix[i]
        
        
        print(res)
        return res
