# Define the Solution class
class Solution(object):
    # Method 1: Using Set Lookup
    def missingNumber_method1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Get the length of the array
        n = len(nums)

        # Convert array to a set for fast lookup
        num_set = set(nums)

        # Check each number from 0 to n
        for i in range(n + 1):
            # If a number is not in the set, it's missing
            if i not in num_set:
                return i

    # Method 2: Using Sum Formula
    def missingNumber_method2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Get the length of the array
        n = len(nums)

        # Sum of first n natural numbers using the formula
        expected_sum = n * (n + 1) // 2

        # Sum of all elements in the given array
        actual_sum = sum(nums)

        # The missing number is the difference between expected and actual sum
        return expected_sum - actual_sum


# Create an instance of the Solution class
sol = Solution()

# Input list (hardcoded)
nums = [3, 0, 1]

# Call both methods and print results
result1 = sol.missingNumber_method1(nums)
print("Result using Method 1 (Set Lookup):", result1)

result2 = sol.missingNumber_method2(nums)
print("Result using Method 2 (Sum Formula):", result2)
