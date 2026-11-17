from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(x)}#{x}" for x in strs)

    def decode(self, s: str) -> List[str]:
        decodedStrs = []
        countStr = ""
        startIndex = 0
        readingLength = True

        for index, value in enumerate(s):

            if readingLength:

                if value == "#":
                    startIndex = index + 1
                    readingLength = False

                    if int(countStr) == 0:
                        decodedStrs.append("")
                        countStr = ""
                        readingLength = True

                else:
                    countStr += value

            else:
                length = int(countStr)

                if index == startIndex + length - 1:
                    decodedStrs.append(s[startIndex : startIndex + length])
                    countStr = ""
                    readingLength = True

        return decodedStrs