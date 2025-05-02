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

# This code defines a class Solution with a method longestCommonSubsequence that takes two strings as input and returns the length of their longest common subsequence. 
# The method uses dynamic programming to build a 2D array dp where dp[i][j] represents the length of the longest common subsequence of the first i characters of text1 and the first j characters of text2.
# The final result is stored in dp[m][n], where m and n are the lengths of text1 and text2, respectively.
# The time complexity of this solution is O(m*n) 
# The space complexity is O(m*n), where m and n are the lengths of text1 and text2, respectively.