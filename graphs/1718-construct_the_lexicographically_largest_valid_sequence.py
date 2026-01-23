#1718. Construct the Lexicographically Largest Valid Sequence
#Medium
#
#Given an integer n, find a sequence that satisfies all of the following:
#
#- The integer 1 occurs once in the sequence.
#- Each integer between 2 and n occurs twice in the sequence.
#- For every integer i between 2 and n, the distance between the two
#  occurrences of i is exactly i.
#
#The distance between two numbers on the sequence, a[i] and a[j], is the
#absolute difference of their indices, |j - i|.
#
#Return the lexicographically largest sequence. It is guaranteed that under the
#given constraints, there is always a solution.
#
#Example 1:
#Input: n = 3
#Output: [3,1,2,3,2]
#
#Example 2:
#Input: n = 5
#Output: [5,3,1,4,3,5,2,4,2]
#
#Constraints:
#    1 <= n <= 20

from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        """
        Backtracking - try larger numbers first for lexicographically largest.
        """
        length = 2 * n - 1
        result = [0] * length
        used = [False] * (n + 1)

        def backtrack(pos: int) -> bool:
            # Skip filled positions
            while pos < length and result[pos] != 0:
                pos += 1

            if pos == length:
                return True

            # Try numbers from n down to 1 (for lexicographically largest)
            for num in range(n, 0, -1):
                if used[num]:
                    continue

                if num == 1:
                    # 1 only appears once
                    result[pos] = 1
                    used[1] = True

                    if backtrack(pos + 1):
                        return True

                    result[pos] = 0
                    used[1] = False
                else:
                    # num > 1: second occurrence at pos + num
                    second_pos = pos + num
                    if second_pos < length and result[second_pos] == 0:
                        result[pos] = num
                        result[second_pos] = num
                        used[num] = True

                        if backtrack(pos + 1):
                            return True

                        result[pos] = 0
                        result[second_pos] = 0
                        used[num] = False

            return False

        backtrack(0)
        return result


class SolutionIterative:
    def constructDistancedSequence(self, n: int) -> List[int]:
        """
        Iterative backtracking with explicit stack.
        """
        length = 2 * n - 1
        result = [0] * length
        used = set()

        # Stack: (position, numbers_to_try_from)
        stack = [(0, n)]

        while stack:
            pos, start_num = stack.pop()

            # Clear any previous choices at this position
            if result[pos] != 0:
                num = result[pos]
                if num > 1:
                    result[pos + num] = 0
                result[pos] = 0
                used.discard(num)

            # Skip filled positions
            while pos < length and result[pos] != 0:
                pos += 1

            if pos == length:
                return result

            # Try numbers from start_num down to 1
            found = False
            for num in range(start_num, 0, -1):
                if num in used:
                    continue

                if num == 1:
                    result[pos] = 1
                    used.add(1)
                    stack.append((pos, num - 1))  # For backtracking
                    stack.append((pos + 1, n))  # Next position
                    found = True
                    break
                else:
                    second_pos = pos + num
                    if second_pos < length and result[second_pos] == 0:
                        result[pos] = num
                        result[second_pos] = num
                        used.add(num)
                        stack.append((pos, num - 1))  # For backtracking
                        stack.append((pos + 1, n))  # Next position
                        found = True
                        break

            if not found and stack:
                # Backtrack
                continue

        return result
