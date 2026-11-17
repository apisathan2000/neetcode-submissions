from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = "".join(f"{len(x)}#{x}" for x in strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        # 12#Knowledgable6#Wisdom11#Criticality15#JustARandomWord
        print(s)

        decodedStrings = []
        strsize = ""
        index = 0

        while index < len(s):
            if s[index].isnumeric():
                strsize += s[index]
                index += 1

            else:
                if s[index] == "#":

                    starttingIndex = index + 1
                    finishingIndex = index + 1 + int(strsize)

                    decodedStrings.append(s[starttingIndex:finishingIndex])
                    strsize = ""
                    index = finishingIndex

        return decodedStrings