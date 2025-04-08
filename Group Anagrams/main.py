from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagram_dict[key].append(word)

        return list(anagram_dict.values())

if __name__ == "__main__":
    sol = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = sol.groupAnagrams(strs)
    print("Grouped Anagrams:", result)
