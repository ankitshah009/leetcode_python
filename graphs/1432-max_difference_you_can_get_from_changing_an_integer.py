#1432. Max Difference You Can Get From Changing an Integer
#Medium
#
#You are given an integer num. You will apply the following steps exactly two
#times:
#    Pick a digit x (0 <= x <= 9).
#    Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
#    Replace all the occurrences of x in the decimal representation of num by y.
#    The new integer cannot have any leading zeros, also the new integer cannot
#    be 0.
#
#Let a and b be the results of applying the operations to num the first and
#second time, respectively.
#
#Return the max difference between a and b.
#
#Example 1:
#Input: num = 555
#Output: 888
#Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
#The second time pick x = 5 and y = 1 and store the new integer in b.
#We have now a = 999 and b = 111 and max difference = 888
#
#Example 2:
#Input: num = 9
#Output: 8
#Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
#The second time pick x = 9 and y = 1 and store the new integer in b.
#We have now a = 9 and b = 1 and max difference = 8
#
#Constraints:
#    1 <= num <= 10^8

class Solution:
    def maxDiff(self, num: int) -> int:
        """
        To maximize a: replace first non-9 digit with 9
        To minimize b: replace first digit > 1 with 1 (if first digit)
                       or replace first digit > 0 (not equal to first) with 0
        """
        s = str(num)

        # Maximize: replace first non-9 digit with 9
        a = s
        for d in s:
            if d != '9':
                a = s.replace(d, '9')
                break

        # Minimize: be careful about leading zeros
        b = s
        if s[0] != '1':
            # Replace first digit with 1
            b = s.replace(s[0], '1')
        else:
            # First digit is 1, find first digit > 1 and not equal to first digit
            for d in s[1:]:
                if d != '0' and d != '1':
                    b = s.replace(d, '0')
                    break

        return int(a) - int(b)


class SolutionExplicit:
    def maxDiff(self, num: int) -> int:
        """More explicit version"""
        s = str(num)

        # Find max value
        max_val = num
        for old in '012345678':  # Try replacing each digit
            new_s = s.replace(old, '9')
            max_val = max(max_val, int(new_s))

        # Find min value (no leading zeros, not zero)
        min_val = num
        for i, d in enumerate(s):
            if i == 0:
                # First digit can only be replaced with non-zero
                for new_d in '123456789':
                    if new_d != d:
                        new_s = s.replace(d, new_d)
                        min_val = min(min_val, int(new_s))
            else:
                # Other digits can be replaced with anything
                for new_d in '0123456789':
                    if new_d != d:
                        # Make sure no leading zero
                        if d == s[0] and new_d == '0':
                            continue
                        new_s = s.replace(d, new_d)
                        if new_s[0] != '0':
                            min_val = min(min_val, int(new_s))

        return max_val - min_val


class SolutionGreedy:
    def maxDiff(self, num: int) -> int:
        """Greedy approach"""
        s = str(num)
        n = len(s)

        # Max: replace leftmost non-9 with 9
        max_s = s
        for i in range(n):
            if s[i] != '9':
                max_s = s.replace(s[i], '9')
                break

        # Min: replace leftmost "replaceable" digit
        min_s = s
        if s[0] != '1':
            # Replace first digit with 1
            min_s = s.replace(s[0], '1')
        else:
            # Find first digit after position 0 that is not 0 or 1
            for i in range(1, n):
                if s[i] not in '01':
                    min_s = s.replace(s[i], '0')
                    break

        return int(max_s) - int(min_s)
