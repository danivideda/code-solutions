import enum
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # Value : index
        for index, num in enumerate(nums):
            difference = target - num
            if difference in prevMap:
                # If the difference exist in previous map, then return the index for the answer
                return [prevMap[difference], index]

            prevMap[num] = index


list = [1, 2, 3]
target = 5
print(Solution().twoSum(list, target))
