from typing import List


class Solution:
    def TwoSum(self, nums: List[int], target: int)-> List[int]:
        Hash = {}  # Dictionary to store number and its index

        for i, n in enumerate(nums):
            diff = target - n  # Compute the required pair value

            if diff in Hash:
                return [Hash[diff], i]  # Return indices if found
            Hash[n] = i  # Store the current number and its index
        return[]  # Just to avoid syntax error if no return occurs (edge case)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    target = 7
    sol = Solution()
    result = sol.TwoSum(nums, target)
    print("Result:", result)


