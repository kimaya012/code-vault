class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        dp=[[0] * (n+1) for x in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        return dp[m][n]

# This is a dynamic programming solution to find the length of the longest common subsequence between two strings.
# The time complexity is O(m*n) and the space complexity is O(m*n), where m and n are the lengths of the two strings.