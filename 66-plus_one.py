#66. Plus One
#Easy
#
#936
#
#1648
#
#Favorite
#
#Share
#Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
#The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#
#You may assume the integer does not contain any leading zero, except the number 0 itself.
#
#Example 1:
#
#Input: [1,2,3]
#Output: [1,2,4]
#Explanation: The array represents the integer 123.
#Example 2:
#
#Input: [4,3,2,1]
#Output: [4,3,2,2]
#Explanation: The array represents the integer 4321.


import functools
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, list(str(functools.reduce(lambda x, y: 10*x+y, digits)+1))))


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(i) for i in str(int(''.join([str(j) for j in digits]))+1)]
