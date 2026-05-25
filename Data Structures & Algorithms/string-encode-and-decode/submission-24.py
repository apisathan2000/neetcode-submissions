from typing import List


class Solution:

    def encode(this, strs: List[str]) -> str:

        sizes = []
        res = ""

        for s in strs:
            sizes.append(len(s))

        for sz in sizes:
            res = res + str(sz) + ","

        res += "#"

        for s in strs:
            res = res + s

        return res

    def decode(this, s: str) -> List[str]:
        if not s:
            return []

        i = 0
        sizes = []
        res = []

        while s[i] != "#":
            cur = ""
            while s[i] != ",":
                cur += s[i]

                i = i + 1

            sizes.append(int(cur))
            i = i + 1

        i = i + 1

        for sz in sizes:
            res.append(s[i : i + sz])
            i += sz

        print(res)

        return res