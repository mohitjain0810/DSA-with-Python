class Solution(object):
    def majorityElement(self, nums):
        # Solution - 1: Using HashMap (dictionary)
        # count = {}
        # res, maxCount = 0, 0

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        #     if count[n] > maxCount:
        #         res = n
        #         maxCount = count[n]
        # return res

        # Solution - 2: Boyer-Moore Voting Algorithm (Optimal)
        res = 0
        count = 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if res == n else -1)
        return res


# Main method
if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    sol = Solution()
    result = sol.majorityElement(nums)
    print("Majority Element:", result)