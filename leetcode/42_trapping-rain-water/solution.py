from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        while l < r:
            print("l: {}, r: {}, leftMax: {}, rightMax: {}".format(
                l, r, leftMax, rightMax))
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res


# height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [2, 0, 0, 0, 1]
height = [5, 4, 1, 2]
# height = [5,4,1,2,3]
print(Solution().trap(height))
