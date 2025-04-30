class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            t=len(str(nums[i]))
            if t % 2 == 0:
                count+=1
        return count
        #Time complexity: O(n)
        #Space complexity: O(1)