from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list) # {char_count : [str]}
        for str in strs:

            # Create the key
            char_count = [0] * 26 # the number of a - z in lowercase
            for char in str:
                char_count[ord(char) - ord('a')] += 1
            key = tuple(char_count)

            # Append the str with the corresponding key
            dict[key].append(str)
        
        return list(dict.values())

strs = ["act","pots","tops","cat","stop","hat"]

print(Solution().groupAnagrams(strs))

