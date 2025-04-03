# Input values (no user input, hardcoded)
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3


# Define the Solution class
class Solution(object):
    # Define the rotate method to rotate the array
    def rotate(self, nums, k):
        n = len(nums)
        # Ensure k is within the length of the array
        k = k % n

        # Helper function to reverse elements in a given range
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the entire array
        reverse(0, n - 1)
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the remaining n - k elements
        reverse(k, n - 1)


# Create an instance of the Solution class
sol = Solution()

# Call the rotate method with hardcoded inputs
sol.rotate(nums, k)

# Print the rotated array
print("Rotated Array:", nums)
