class Solution:
    def findLHS(self, nums):
        hash = {}
        longest = 0
        for num in nums:
            hash[num] = hash.get(num, 0) + 1
        for key in hash:
            if key + 1 in hash:
                longest = max(longest, hash[key] + hash[key + 1])
        return longest