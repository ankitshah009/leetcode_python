#753. Cracking the Safe
#Hard
#
#There is a safe protected by a password. The password is a sequence of n digits
#where each digit can be in the range [0, k - 1].
#
#The safe has a peculiar way of checking the password. When you enter in a
#sequence, it checks the most recent n digits entered each time you type a digit.
#
#For example, the correct password is "345" and you enter in "012345":
#- After typing 0, the most recent 3 digits is "0", which is incorrect.
#- After typing 1, the most recent 3 digits is "01", which is incorrect.
#- After typing 2, the most recent 3 digits is "012", which is incorrect.
#- After typing 3, the most recent 3 digits is "123", which is incorrect.
#- After typing 4, the most recent 3 digits is "234", which is incorrect.
#- After typing 5, the most recent 3 digits is "345", which is correct.
#
#Return any string of minimum length that will unlock the safe at some point.
#
#Example 1:
#Input: n = 1, k = 2
#Output: "10"
#Explanation: The password is a single digit, so enter each digit.
#
#Example 2:
#Input: n = 2, k = 2
#Output: "01100"
#Explanation: For each possible password:
#- "00" is typed starting from the 3rd digit.
#- "01" is typed starting from the 4th digit.
#- "10" is typed starting from the 1st digit.
#- "11" is typed starting from the 2nd digit.
#
#Constraints:
#    1 <= n <= 4
#    1 <= k <= 10
#    1 <= k^n <= 4096

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        """
        De Bruijn sequence using Hierholzer's algorithm for Eulerian path.
        """
        if n == 1:
            return ''.join(str(i) for i in range(k))

        # Build graph: edge from node[:n-1] to node[1:]
        # Each node is a string of length n-1
        visited = set()
        result = []

        def dfs(node):
            for digit in range(k):
                edge = node + str(digit)
                if edge not in visited:
                    visited.add(edge)
                    dfs(edge[1:])
                    result.append(str(digit))

        start = '0' * (n - 1)
        dfs(start)

        return ''.join(result[::-1]) + start


class SolutionIterative:
    """Iterative Hierholzer's algorithm"""

    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return ''.join(str(i) for i in range(k))

        visited = set()
        result = []
        stack = ['0' * (n - 1)]

        while stack:
            node = stack[-1]
            found = False

            for digit in range(k):
                edge = node + str(digit)
                if edge not in visited:
                    visited.add(edge)
                    stack.append(edge[1:])
                    found = True
                    break

            if not found:
                result.append(stack.pop()[-1])

        return ''.join(result[:-1][::-1]) + '0' * (n - 1)


class SolutionLyndonWord:
    """Using Lyndon words for De Bruijn sequence"""

    def crackSafe(self, n: int, k: int) -> str:
        # Martin's algorithm for De Bruijn sequence
        alphabet = ''.join(str(i) for i in range(k))
        a = [0] * (k * n)
        sequence = []

        def db(t, p):
            if t > n:
                if n % p == 0:
                    sequence.extend(a[1:p+1])
            else:
                a[t] = a[t - p]
                db(t + 1, p)
                for j in range(a[t - p] + 1, k):
                    a[t] = j
                    db(t + 1, t)

        db(1, 1)
        result = ''.join(alphabet[i] for i in sequence)
        return result + result[:n-1]
