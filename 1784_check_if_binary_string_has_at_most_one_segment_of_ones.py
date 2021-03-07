#1784. Check if Binary String Has at Most One Segment of Ones
#Easy
#
#Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.
#
# 
#
#Example 1:
#
#Input: s = "1001"
#Output: false
#Explanation: The ones do not form a contiguous segment.
#
#Example 2:
#
#Input: s = "110"
#Output: true
#
# 
#
#Constraints:
#
#    1 <= s.length <= 100
#    s[i]​​​​ is either '0' or '1'.
#    s[0] is '1'.
#


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        num = int(s, 2)
        print(num&-num)
        num += (num & -num)
        return num & (num - 1) == 0

Solution 1

Time O(n), space O(1).

Python

    def checkOnesSegment(self, s):
        return '01' not in s


Solution 2

If strip all 0s, it should left only 1s
Then strip 1s, nothing left.

I don't know why, but string s doesn't have leading zeros.
This solution also works for s with leading zeros.

Time O(n), space O(n)

Python

    def checkOnesSegment(self, s):
        return not s.strip('0').strip('1')

