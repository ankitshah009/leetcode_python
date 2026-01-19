#1442. Count Triplets That Can Form Two Arrays of Equal XOR
#Medium
#
#Given an array of integers arr.
#
#We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
#
#Let's define a and b as follows:
#    a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
#    b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
#
#Note that ^ denotes the bitwise-xor operation.
#
#Return the number of triplets (i, j and k) Where a == b.
#
#Example 1:
#Input: arr = [2,3,1,6,7]
#Output: 4
#Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
#
#Example 2:
#Input: arr = [1,1,1,1,1]
#Output: 10
#
#Constraints:
#    1 <= arr.length <= 300
#    1 <= arr[i] <= 10^8

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # a == b means a ^ b == 0
        # arr[i] ^ ... ^ arr[j-1] ^ arr[j] ^ ... ^ arr[k] == 0
        # So we need XOR from i to k to be 0

        n = len(arr)
        count = 0

        # prefix[i] = XOR of arr[0..i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]

        # For each pair (i, k) where prefix[i] == prefix[k+1],
        # any j in range (i, k] works
        # Number of valid j's = k - i

        for i in range(n):
            for k in range(i + 1, n):
                if prefix[i] == prefix[k + 1]:
                    count += k - i

        return count
