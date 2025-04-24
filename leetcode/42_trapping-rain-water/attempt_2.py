from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        p_l, p_r = 1, len(height) - 2
        max_l, max_r = height[p_l - 1], height[p_r + 1]

        min_h = min(max_l, max_r)
        ptr = 0
        if min_h == max_l:
            ptr = p_l
        else:
            ptr = p_r

        while p_l <= p_r:
            # print("(p_l: {}), (p_r: {}), (max_l: {}), (max_r: {}), (ptr: {}), (min_h: {})".format(
            #     p_l, p_r, max_l, max_r, ptr, min_h))

            # Calculate current water in ptr
            calc = min_h - height[ptr]
            if calc > 0:
                water += calc
            # Update both max_l and max_r
            max_l = max(max_l, height[p_l])
            max_r = max(max_r, height[p_r])
            # Move the ptr of the smaller between max_l and max_r
            min_h = min(max_l, max_r)
            if min_h == max_l:
                ptr = p_l + 1
                p_l += 1
            else:
                ptr = p_r - 1
                p_r -= 1

        return water


# height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [2, 0, 0, 0, 1]
height = [5,4,1,2]
# height = [5,4,1,2,3]
print(Solution().trap(height))
