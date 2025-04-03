class Solution(object):
    def removeDuplicates(self, nums):
        l = 1  # Slow pointer starts from index 1
        for r in range(1, len(nums)):  # Fast pointer starts from index 1
            if nums[r] != nums[r - 1]:  # If new unique element is found
                nums[l] = nums[r]  # Place unique element at the next position
                l += 1  # Move slow pointer
        return l  # Return the count of unique elements

# Main function to test the code
if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 4, 4, 5]  # Example input
    solution = Solution()  # Create an instance of the Solution class
    k = solution.removeDuplicates(nums)  # Call the method
    print("Number of unique elements:", k)
    print("Modified array:", nums[:k])  # Printing only the unique part
