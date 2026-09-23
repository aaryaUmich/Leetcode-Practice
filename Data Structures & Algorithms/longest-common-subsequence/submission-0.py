class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #memo[i][j] represents the longest common subsequence at our current point, which is up through index i in text 1, and up through index j in text2
        memo = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

        #base cases
        #memo[0][i] and memo[i][0] = 0


        #recurrence relation: memo[i][j] = memo[i-1][j-1]+1 if text1[i-1]==text2[j-1]
        #if text1[i-1]!=text2[j-1] memo[i][j] = max(memo[i-1][j], memo[i][j-1])

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    memo[i][j] = memo[i-1][j-1]+1
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
        
        return memo[len(text1)][len(text2)]

