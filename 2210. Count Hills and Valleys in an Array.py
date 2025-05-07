class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        h=0
        v=0
        num=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                num.append(nums[i])
        n=len(num)
        for i in range(1,n-1):
            if (num[i] > num[i+1] and num[i] > num[i-1]):
                h+=1
            if (num[i] < num[i+1] and num[i] < num[i-1]):
                v+=1
        return (h+v)

# 0ms, 100% faster than 100% of Python3 submissions
