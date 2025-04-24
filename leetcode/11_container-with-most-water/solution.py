from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        res = 0
        while l < r:
            mh = min(height[l], height[r])
            res = max(res, mh * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res

# height = [1,7,2,5,4,7,3,6]
height = [2,2,2]
print(Solution().maxArea(height))