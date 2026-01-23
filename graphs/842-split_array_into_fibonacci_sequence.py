#842. Split Array into Fibonacci Sequence
#Medium
#
#You are given a string of digits num. Return any possible Fibonacci-like
#sequence split from num, or return [] if it is not possible.
#
#A Fibonacci-like sequence is a list F of non-negative integers such that:
#- 0 <= F[i] < 2^31
#- F.length >= 3
#- F[i] + F[i+1] == F[i+2] for all 0 <= i < F.length - 2.
#
#Also, note that when splitting num into the sequence, leading zeros are not
#allowed, unless the number itself is 0.
#
#Example 1:
#Input: num = "1101111"
#Output: [11,0,11,11]
#or [110, 1, 111] is also valid
#
#Example 2:
#Input: num = "112358130"
#Output: []
#Explanation: The task is impossible.
#
#Example 3:
#Input: num = "0123"
#Output: []
#Explanation: Leading zeros are not allowed.
#
#Constraints:
#    1 <= num.length <= 200
#    num contains only digits.

class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        """
        Backtracking: try all possible first two numbers.
        """
        MAX_VAL = 2**31 - 1
        n = len(num)
        result = []

        def backtrack(idx, seq):
            if idx == n:
                return len(seq) >= 3

            # Determine expected next number
            max_len = 10 if num[idx] != '0' else 1  # No leading zeros except "0"

            for length in range(1, min(max_len, n - idx) + 1):
                s = num[idx:idx + length]
                val = int(s)

                if val > MAX_VAL:
                    break

                if len(seq) >= 2:
                    expected = seq[-1] + seq[-2]
                    if val > expected:
                        break
                    if val < expected:
                        continue

                seq.append(val)
                if backtrack(idx + length, seq):
                    return True
                seq.pop()

            return False

        backtrack(0, result)
        return result


class SolutionIterative:
    """Try all first two numbers"""

    def splitIntoFibonacci(self, num: str) -> list[int]:
        MAX_VAL = 2**31 - 1
        n = len(num)

        for i in range(1, n):
            if num[0] == '0' and i > 1:
                break

            for j in range(i + 1, n):
                if num[i] == '0' and j - i > 1:
                    break

                first = int(num[:i])
                second = int(num[i:j])

                if first > MAX_VAL or second > MAX_VAL:
                    continue

                seq = [first, second]
                k = j

                while k < n:
                    next_val = seq[-1] + seq[-2]
                    if next_val > MAX_VAL:
                        break

                    next_str = str(next_val)
                    if not num[k:].startswith(next_str):
                        break

                    seq.append(next_val)
                    k += len(next_str)

                if k == n and len(seq) >= 3:
                    return seq

        return []
