#1310. XOR Queries of a Subarray
#Medium
#
#You are given an array arr of positive integers. You are also given the array
#queries where queries[i] = [lefti, righti].
#
#For each query i compute the XOR of elements from lefti to righti (that is,
#arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti]).
#
#Return an array answer where answer[i] is the answer to the ith query.
#
#Example 1:
#Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
#Output: [2,7,14,8]
#Explanation:
#The binary representation of the elements in the array are:
#1 = 0001, 3 = 0011, 4 = 0100, 8 = 1000
#The XOR values for queries are:
#[0,1] = 1 xor 3 = 2
#[1,2] = 3 xor 4 = 7
#[0,3] = 1 xor 3 xor 4 xor 8 = 14
#[3,3] = 8
#
#Example 2:
#Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
#Output: [8,0,4,14]
#
#Constraints:
#    1 <= arr.length, queries.length <= 3 * 10^4
#    1 <= arr[i] <= 10^9
#    queries[i].length == 2
#    0 <= lefti <= righti < arr.length

from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """
        Use prefix XOR.
        XOR[l,r] = prefix[r+1] ^ prefix[l]
        Because XOR is self-inverse: a ^ a = 0
        """
        n = len(arr)

        # Build prefix XOR
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]

        # Answer queries
        return [prefix[r + 1] ^ prefix[l] for l, r in queries]


class SolutionInPlace:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """Modify arr in place to store prefix XOR"""
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]

        result = []
        for l, r in queries:
            if l == 0:
                result.append(arr[r])
            else:
                result.append(arr[r] ^ arr[l - 1])

        return result
