from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            # If the sum is greater than the target, then decrease the sum by moving the 'right' pointer
            if numbers[l] + numbers[r] > target:
                r -= 1
            # If the sum is smaller than the target, then increase the sum by moving the 'left' pointer
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]


numbers = [2, 7, 11, 15]
target = 18

print(Solution().twoSum(numbers, target))
