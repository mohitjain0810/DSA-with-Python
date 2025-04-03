# Define the Solution class
class Solution(object):
    # Method 1: Using String Manipulation
    def isPalindrome_method1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Create a new string with only alphanumeric characters in lowercase
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()

        # Check if the string is equal to its reverse
        return newStr == newStr[::-1]

    # Method 2: Using Two Pointers
    def isPalindrome_method2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1

        # Compare characters from both ends using two pointers
        while left < right:
            # Move left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare the characters (ignoring case)
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True


# Create an instance of the Solution class
sol = Solution()

# Input string (hardcoded)
s = "A man, a plan, a canal: Panama"

# Call both methods and print results
result1 = sol.isPalindrome_method1(s)
print("Result using Method 1 (String Manipulation):", result1)

result2 = sol.isPalindrome_method2(s)
print("Result using Method 2 (Two Pointers):", result2)
