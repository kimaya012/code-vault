def buildArray(self, nums: List[int]) -> List[int]:
    ans=[]
    for i in range(len(nums)):
        ans.append(nums[nums[i]])
    return ans

# 0ms, 100% faster than 100% of Python3 submissions
# 1.4MB, less than 100% of Python3 submissions
