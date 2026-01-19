# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
#1663. Smallest String With A Given Numeric Value
#Medium
#
#The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.
#
#The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.
#
#You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.
#
#Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.
#
# 
#
#Example 1:
#
#Input: n = 3, k = 27
#Output: "aay"
#Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the smallest string with such a value and length equal to 3.
#
#Example 2:
#
#Input: n = 5, k = 73
#Output: "aaszz"
#
# 
#
#Constraints:
#
#    1 <= n <= 105
#    n <= k <= 26 * n
#
#

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        num2 = (k-n) // 25
        num1 = n - num2 - 1
        num = k - (num1 + num2 * 26)
        return 'a' * num1 + chr(num+96) + 'z' * num2
                    
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = ['a'] * n
        k = k - n
        z = k // 25                  # number of "z" which we can have
        leftover = k % 25       # for the remaining characters
        s[n - 1 - z] = chr(ord('a') + leftover)
        return "".join(s[:n - z]) + 'z' * z

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ['a'] * n
        k, i = k-n, n-1
        z, nz = divmod(k, 25)                # `z`: number of *z* I need, `nz`: ascii of the letter just to cover the leftover
        ans[n-1-z] = chr(nz + ord('a'))      # adjust the left over `k` using mod
        return ''.join(ans[:n-z]) + 'z' * z  # make final string & append `z` to the end

##
#Explanation
#
#    So the idea is
#        First, make sure string have enough length n by initializing string with all letters as a of length n
#        Adjust the string so that it can fully cover the given number k
#            We do this by using z from the right side
#        Ultimately, there might have some left over that using z will cause a overflow (k becomes negative)
#            then we use corresponding letter for it
#        for example, n=3, k=29
#            start with aaa, now k is 26
#            start putting z from the right, we can get aaz, now k is 1
#            since z will overflow 1, we use b instead, to just cover k
#            final result will be abz
#    ans: final answer in list format; z number of z I need, nz the letter just to cover the left over
###
