from typing import List


class Solution:

    def encode(this, strs: List[int]) -> str:

        sizes: List[int] = []
        res: str = ""

        for x in strs:
            sizes.append(len(x))

        for sz in sizes:
            res += str(sz)
            res += ","

        res += "#"
        for x in strs:
            res += x

        return res

    def decode(this, s: str) -> List[str]:
        
        splitted = s.split('#' , maxsplit=1)

        sizes = []
        originalList = []
        indicator = 0
        
        for sz in splitted[0].split(","):
            if sz != "":
                sizes.append(int(sz))

        for sz in sizes:
            originalList.append(splitted[1][indicator : sz + indicator])
            indicator += sz

        print(originalList)
        return originalList

