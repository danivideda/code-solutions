from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSums = a + nums[l] + nums[r]
                if threeSums < 0:
                    l += 1
                elif threeSums > 0:
                    r -= 1
                else:
                    result.append([a, nums[l], nums[r]])

                    # Only check one of the pointer for duplication,
                    # since the corresponding 'sums' will be automatically different
                    # and then handled by the above if statements
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return result


# nums = [-3, 3, 4, -3, 1, 2]
nums = [-1, 0, 1, 2, -1, -4]
# nums = [0, 1, 1]
# nums = [0, 0, 0]
print(Solution().threeSum(nums))
