class Solution:
    def longestPalindrome(self, s: str) -> str:
        #2d bcuz we have to keep track of two things, left and right pointer within s
        #memo[i][j] will be a bool, and will represent wether the substring between i and j is a valid palindrome

        memo = [[False] * len(s) for _ in range(len(s))]
        coords = (0,0)
        curr_max = -999999999
        
        
        #recurrence relation: if j>i+1 memo[i][j] = true if s[i]==s[j] and memo[i+1][j-1]
        #i==j true --> base case
        #if j==i+1 --> if s[i]==s[j] --> true

        for length in range(1,len(s)+1):
            for i in range(0,len(s)-length+1):
                j = i+length-1
                if i==j:
                    memo[i][j] = True
                elif i+1==j:
                    if s[i]==s[j]:
                        memo[i][j] = True
                elif j>i+1:
                    if s[i]==s[j] and memo[i+1][j-1] == True:
                        memo[i][j] = True
        
        for i in range(0,len(s)):
            for j in range(0,len(s)):
                if memo[i][j] == True:
                    if j-i+1>curr_max:
                        curr_max = j-i+1
                        coords = (i,j)
    


        return s[coords[0]:coords[1]+1]

        


        


