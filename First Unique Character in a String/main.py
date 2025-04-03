# Function to find the first non-repeating character's index
def firstUniqChar(s):
    # Step 1: Create a frequency dictionary
    char_count = {}

    # Count occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Step 2: Find the first non-repeating character and return its index
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i  # Return index of first unique character

    return -1  # If no unique character exists


# Main function
def main():
    # Test cases
    test_strings = ["leetcode", "loveleetcode", "aabb"]

    for s in test_strings:
        result = firstUniqChar(s)
        print(f"Input: \"{s}\" → Output: {result}")


# Run the main function
if __name__ == "__main__":
    main()
