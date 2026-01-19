#344. Reverse String
#Easy
#
#842
#
#544
#
#Favorite
#
#Share
#Write a function that reverses a string. The input string is given as an array of characters char[].
#
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
#You may assume all the characters consist of printable ascii characters.
#
# 
#
#Example 1:
#
#Input: ["h","e","l","l","o"]
#Output: ["o","l","l","e","h"]
#Example 2:
#
#Input: ["H","a","n","n","a","h"]
#Output: ["h","a","n","n","a","H"]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start,end = 0,len(s)-1
        while(start<end):
            s[start],s[end] = s[end],s[start]
            start += 1
            end -= 1

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[::]=s[::-1];

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(l, r, s):
            if l >= r:
                return s
            s[l], s[r] = s[r], s[l]        
            return helper(l+1, r-1, s)
        helper(0, len(s)-1, s) 

