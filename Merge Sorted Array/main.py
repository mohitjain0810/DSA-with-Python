# Input values (no user input, hardcoded)
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


# Define the Solution class
class Solution(object):
    # Define the merge method to merge two sorted arrays
    def merge(self, nums1, m, nums2, n):
        # Last index to fill in nums1
        last = m + n - 1

        # Merge in reverse order from the end
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # Fill nums1 with remaining nums2 elements if any
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1


# Create an instance of the Solution class
sol = Solution()

# Call the merge method with hardcoded inputs
sol.merge(nums1, m, nums2, n)

# Print the merged array
print("Merged Array:", nums1)
