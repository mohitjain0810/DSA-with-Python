# Get input from the user as a list of integers
nums = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))


# Define the Solution class
class Solution(object):
    # Define the maxSubArray method to calculate the maximum subarray sum
    def maxSubArray(self, nums):
        # Initialize the maximum subarray sum with the first element
        maxSub = nums[0]
        # Initialize cumulative sum to 0
        cumSum = 0

        # Loop through each element in the array
        for n in nums:
            # If cumulative sum is negative, reset to 0
            if cumSum < 0:
                cumSum = 0
            # Add the current element to cumulative sum
            cumSum += n
            # Update maxSub with the maximum value between maxSub and cumSum
            maxSub = max(maxSub, cumSum)

        # Return the maximum subarray sum
        return maxSub


# Create an instance of the Solution class
sol = Solution()

# Call the maxSubArray method with user input and print the result
result = sol.maxSubArray(nums)
print("Maximum Subarray Sum:", result)
