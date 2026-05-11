from typing import List

class Solution:
    def hasDuplicate (this, nums:List[int])->bool: 
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)

            
        return False