from typing import List
import collections

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = collections.deque()
        lp, rp = 0, len(nums) - 1
        
        while lp <= rp:
            left_val, right_val = abs(nums[lp]), abs(nums[rp])
            if left_val < right_val:
                res.appendleft(right_val * right_val)
                rp -= 1
            else:
                res.appendleft(left_val * left_val)
                lp += 1
        
        return list(res)
