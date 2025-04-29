#SOLUTION1:
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def rec(s, idx):
            if idx == len(s):
                return True
            for i in range(idx+1, len(s)+1):
                if s[idx:i] in wordDict and rec(s, i):
                    return True
            return False
        
        return rec(s, 0)
#However, this recursive solution is not efficient for larger strings and word dictionaries.
# A more efficient solution would be to use dynamic programming to store the results of subproblems.


#SOLUTION2:
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def rec(idx):
            if idx == len(s):
                return True
            if idx in memo:
                return memo[idx]
            
            for i in range(idx + 1, len(s) + 1):
                if s[idx:i] in wordDict and rec(i):
                    memo[idx] = True
                    return True
            
            memo[idx] = False
            return False
        
        return rec(0)
# This solution uses memoization to store the results of subproblems, which significantly reduces the time complexity.
# The time complexity of this solution is O(n^2) in the worst case, where n is the length of the string s.
# The space complexity is O(n) due to the memoization dictionary.
