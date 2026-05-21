from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for x in strs:
            final_str = final_str + str(len(x)) + "#" + x

        return final_str

    def decode(self, s: str) -> List[str]:

        original_list = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            original_list.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return original_list