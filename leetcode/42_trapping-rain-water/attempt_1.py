from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        highest = max(height)
        l, r = 0, len(height) - 1

        water = 0

        for altitude in range(1, highest + 1):
            while height[l] < altitude:
                l += 1
            
            while height[r] < altitude:
                r -= 1
            
            if l >= r:
                break
            
            # print("alt:", altitude, "l:", l, "r:", r)

            for index in range(l+1, r+1):
                if height[index] < altitude:
                    water += 1
        
        return water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))

