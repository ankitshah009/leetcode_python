#961. N-Repeated Element in Size 2N Array
#Easy
#
#In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
#
#Return the element repeated N times.
#
# 
#
#Example 1:
#
#Input: [1,2,3,3]
#Output: 3
#
#Example 2:
#
#Input: [2,1,2,5,3,2]
#Output: 2
#
#Example 3:
#
#Input: [5,1,5,2,5,3,5,4]
#Output: 5
#
# 
#
#Note:
#
#    4 <= A.length <= 10000
#    0 <= A[i] < 10000
#    A.length is even
#

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        return int((sum(A)-sum(set(A))) // (len(A)//2-1))


class Solution(object):
    def repeatedNTimes(self, A):
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1:
                return k

Approach 2: Compare

Intuition and Algorithm

If we ever find a repeated element, it must be the answer. Let's call this answer the major element.

Consider all subarrays of length 4. There must be a major element in at least one such subarray.

This is because either:

    There is a major element in a length 2 subarray, or;
    Every length 2 subarray has exactly 1 major element, which means that a length 4 subarray that begins at a major element will have 2 major elements.

Thus, we only have to compare elements with their neighbors that are distance 1, 2, or 3 away.

class Solution(object):
    def repeatedNTimes(self, A):
        for k in xrange(1, 4):
            for i in xrange(len(A) - k):
                if A[i] == A[i+k]:
                    return A[i]
