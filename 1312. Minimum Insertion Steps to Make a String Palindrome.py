class Solution:
    def minInsertions(self, s: str) -> int:
        d={}
        def rec(i,j):
            if i >=j:
                return 0
            if (i,j) in d:#check overlapping subproblems
                return d[(i,j)]
            if s[i] == s[j]:
                d[(i,j)]= rec(i+1,j-1)#re-assign
                return d[(i,j)]
            else:
                d[(i,j)] = 1+min(rec(i+1,j),rec(i,j-1))
                return d[(i,j)]
        return rec(0,len(s)-1)
    
    