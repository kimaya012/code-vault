class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in hash_map:
                return[i,hash_map[diff]]
            hash_map[v] = i
