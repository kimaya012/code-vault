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