from typing import List


class Solution:
    def isValid(self, s: str) -> bool:

        sizeS = len(s)
        closingStack = []

        for i in range(0, sizeS):
            sizeStack = len(closingStack)
            if sizeStack == 0:
                closingStack.append(s[i])
            else:
                print(i)
                if (
                    (closingStack[sizeStack - 1] == "(" and s[i] == ")")
                    or (closingStack[sizeStack - 1] == "[" and s[i] == "]")
                    or (closingStack[sizeStack - 1] == "{" and s[i] == "}")
                ):
                    closingStack.pop()
                else:
                    closingStack.append(s[i])

        return True if len(closingStack) == 0 else False