from typing import List


class Solution:
    def topKFrequent(self, nums:List[int] , k:int)->List[int]:
        
        count_dict = {}
        
        for x in nums:
            
            if x in count_dict:
                count_dict[x] += 1
            else :
                count_dict[x] = 1
                
            
        
        
        sorted_list = sorted(count_dict.items() , key=lambda item:item[1] , reverse=True)
        sorted_dict = dict(sorted_list)
        
        kFrequentList = sorted(list(sorted_dict)[:k])
         
        return kFrequentList
