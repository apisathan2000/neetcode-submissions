
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        letterS = {}
        letterT = {} 

        for x in s:
            if x in letterS:
                letterS[x] += 1
            else:
                letterS[x] = 1
        
        for y in t:
            if y in letterT:
                letterT[y] += 1
            else:
                letterT[y] = 1

        return letterS == letterT





