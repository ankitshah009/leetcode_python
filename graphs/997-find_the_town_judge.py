#997. Find the Town Judge
#Easy
#
#In a town, there are n people labeled from 1 to n. There is a rumor that one
#of these people is secretly the town judge.
#
#If the town judge exists, then:
#1. The town judge trusts nobody.
#2. Everybody (except for the town judge) trusts the town judge.
#3. There is exactly one person that satisfies properties 1 and 2.
#
#You are given an array trust where trust[i] = [ai, bi] representing that person
#ai trusts person bi.
#
#Return the label of the town judge if exists and can be identified, or return
#-1 otherwise.
#
#Example 1:
#Input: n = 2, trust = [[1,2]]
#Output: 2
#
#Example 2:
#Input: n = 3, trust = [[1,3],[2,3]]
#Output: 3
#
#Example 3:
#Input: n = 3, trust = [[1,3],[2,3],[3,1]]
#Output: -1
#
#Constraints:
#    1 <= n <= 1000
#    0 <= trust.length <= 10^4
#    trust[i].length == 2
#    All the pairs trust[i] are unique.
#    ai != bi
#    1 <= ai, bi <= n

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        """
        Count in-degree and out-degree. Judge has in=n-1, out=0.
        """
        if n == 1:
            return 1

        trust_count = [0] * (n + 1)  # in-degree - out-degree

        for a, b in trust:
            trust_count[a] -= 1  # a trusts someone
            trust_count[b] += 1  # b is trusted

        for i in range(1, n + 1):
            if trust_count[i] == n - 1:
                return i

        return -1


class SolutionSeparate:
    """Separate in and out degree"""

    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1:
            return 1

        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)

        for a, b in trust:
            out_degree[a] += 1
            in_degree[b] += 1

        for i in range(1, n + 1):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i

        return -1


class SolutionSet:
    """Using sets"""

    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1:
            return 1

        trusts_someone = set()
        trusted_by = [set() for _ in range(n + 1)]

        for a, b in trust:
            trusts_someone.add(a)
            trusted_by[b].add(a)

        for i in range(1, n + 1):
            if i not in trusts_someone and len(trusted_by[i]) == n - 1:
                return i

        return -1
