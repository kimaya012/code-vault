class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Length of the input string
        m = len(s)
        n = len(s)

        # Reverse the string to compare it with the original
        s1 = s[::-1]

        # Initialize a 2D DP table with dimensions (m+1) x (n+1)
        # dp[i][j] will store the length of the longest common subsequence
        # between s[0..i-1] and s1[0..j-1]
        dp = [[0] * (n + 1) for x in range(m + 1)]

        # Build the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If characters match, add 1 to the result from the previous subproblem
                if s[i - 1] == s1[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # If characters don't match, take the maximum from left or top cell
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        # The bottom-right cell contains the length of the longest palindromic subsequence
        return dp[m][n]
