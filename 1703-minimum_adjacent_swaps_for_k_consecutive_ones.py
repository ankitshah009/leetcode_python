#1703. Minimum Adjacent Swaps for K Consecutive Ones
#Hard
#
#You are given an integer array, nums, and an integer k. nums comprises of only 0's and 1's. In one move, you can choose two adjacent indices and swap their values.
#
#Return the minimum number of moves required so that nums has k consecutive 1's.
#
# 
#
#Example 1:
#
#Input: nums = [1,0,0,1,0,1], k = 2
#Output: 1
#Explanation: In 1 move, nums could be [1,0,0,0,1,1] and have 2 consecutive 1's.
#
#Example 2:
#
#Input: nums = [1,0,0,0,0,0,1,1], k = 3
#Output: 5
#Explanation: In 5 moves, the leftmost 1 can be shifted right until nums = [0,0,0,0,0,1,1,1].
#
#Example 3:
#
#Input: nums = [1,1,0,1], k = 2
#Output: 0
#Explanation: nums already has 2 consecutive 1's.
#
# 
#
#Constraints:
#
#    1 <= nums.length <= 105
#    nums[i] is 0 or 1.
#    1 <= k <= sum(nums)
#
#

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        pos = [p for p,x in enumerate(nums) if x == 1]
        print(pos)

        pos = [p-i for i,p in enumerate(pos)]        
        print(pos)
        
        mid = k//2
        sizeleft = mid
        sizeright = k-1-sizeleft
        
        curleft = sum(abs(x - pos[mid]) for x in pos[:sizeleft])
        curright = sum(abs(x - pos[mid]) for x in pos[mid+1:k])        
        minres = curleft + curright
        
        print(curleft, curright, minres)
        
        for ptr in range(1, len(pos)-k+1):
            # print("ptr", ptr, ptr+mid, ptr+k)
            curleft -= (pos[ptr+mid-1] - pos[ptr-1])
            curleft += (pos[ptr+mid] - pos[ptr+mid-1])*sizeleft
        
            curright -= (pos[ptr+mid] - pos[ptr+mid-1])*sizeright
            curright += (pos[ptr+k-1] - pos[ptr+mid])
        
            minres = min(minres, curleft+curright)
            # print(curleft, curright, minres)
            
        print()
        return minres
