from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return str([])
        
        else:
            final_str = ""

            print(f"Initial List {strs}")

            for x in strs:
                final_str = final_str + "--" + x 

            final_str = final_str.removeprefix("--")

            return final_str

    def decode(self, s: str) -> List[str]:
        print(f"Encoded String => {s}")

        if s == '[]':
            return []
        
        else: 
            original_list = []

            original_list = s.split("--")

            print(f"Final List => {original_list}")

            return original_list

