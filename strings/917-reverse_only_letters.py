#https://leetcode.com/problems/reverse-only-letters/
#917. Reverse Only Letters
#Easy
#
#Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
#
# 
#
#Example 1:
#
#Input: "ab-cd"
#Output: "dc-ba"
#
#Example 2:
#
#Input: "a-bC-dEf-ghIj"
#Output: "j-Ih-gfE-dCba"
#
#Example 3:
#
#Input: "Test1ng-Leet=code-Q!"
#Output: "Qedo1ct-eeLg=ntse-T!"
#

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        ans = []
        j = len(ans) - 1
        for i, x in enumerate(S):
            if x.isalpha():
                while not S[j].isalpha():
                    j -= 1
                ans.append(S[j])
                j -= 1
            else:
                ans.append(x)
        
        return "".join(ans)

class Solution(object):
    def reverseOnlyLetters(self, S):
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)
