#162. Find Peak Element
#Medium
#
#A peak element is an element that is greater than its neighbors.
#
#Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
#
#The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
#You may imagine that nums[-1] = nums[n] = -∞.
#
#Example 1:
#
#Input: nums = [1,2,3,1]
#Output: 2
#Explanation: 3 is a peak element and your function should return the index number 2.
#
#Example 2:
#
#Input: nums = [1,2,1,3,5,6,4]
#Output: 1 or 5 
#Explanation: Your function can return either index number 1 where the peak element is 2, 
#             or index number 5 where the peak element is 6.
#
#Note:
#
#Your solution should be in logarithmic complexity.

class Solution:
    def findPeakElement(self, nums: List[int], base=0) -> int:
        N=len(nums)
        if N == 1:   return base
        if N == 2:
            if nums[0] > nums[1]: return base
            else:               return base + 1
        mid   = (N - 1) // 2
        if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
            # The middle element is a peak.
            return mid + base
        elif nums[mid] < nums[mid-1]:
            # There must be one or more peak(s) in the left part.
            return self.findPeakElement(nums[:mid], base)
        else:
            # There must be one or more peak(s) in the right part.
            return self.findPeakElement(nums[mid+1:], mid + 1 + base)


public class Solution {
    public int findPeakElement(int[] nums) {
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int mid = (l + r) / 2;
            if (nums[mid] > nums[mid + 1])
                r = mid;
            else
                l = mid + 1;
        }
        return l;
    }
}


### 

#    Time complexity : O(log2(n))O\big(log_2(n)\big)O(log2​(n)). We reduce the search space in half at every step. Thus, the total search space will be consumed in log2(n)log_2(n)log2​(n) steps. Here, nnn refers to the size of numsnumsnums array.

#    Space complexity : O(1)O(1)O(1). Constant extra space is used.



public class Solution {
    public int findPeakElement(int[] nums) {
        return search(nums, 0, nums.length - 1);
    }
    public int search(int[] nums, int l, int r) {
        if (l == r)
            return l;
        int mid = (l + r) / 2;
        if (nums[mid] > nums[mid + 1])
            return search(nums, l, mid);
        return search(nums, mid + 1, r);
    }
}
