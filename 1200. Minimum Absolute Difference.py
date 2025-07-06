class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res=[]
        min_diff=float('inf')
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i-1])
        for i in range(1, len(arr)):
            if (arr[i] - arr[i-1]) == min_diff:
                res.append([arr[i-1],arr[i]])
        return res