class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m=len(s)
        n=len(s)
        s1=s[::-1]
        dp=[[0] * (n+1) for x in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == s1[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        return dp[m][n]

# This is a dynamic programming solution to find the length of the longest palindromic subsequence in a string.
# The time complexity is O(n^2) and the space complexity is O(n^2), where n is the length of the string.