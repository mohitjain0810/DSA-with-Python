from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            n = abs(n)
            if nums[n - 1] < 0:
                res.append(n)
            nums[n - 1] = -nums[n - 1]
        return res


if __name__ == "__main__":
    nums = [1, 2, 3, 3, 4, 5, 6, 7, 7]
    sol = Solution()
    result = sol.findDuplicates(nums)
    print("Duplicates:", result)