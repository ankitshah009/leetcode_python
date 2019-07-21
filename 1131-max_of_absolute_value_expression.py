#1131. Maximum of Absolute Value Expression
#Medium
#
#Given two arrays of integers with equal lengths, return the maximum value of:
#
#|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
#
#where the maximum is taken over all 0 <= i, j < arr1.length.
#
# 
#
#Example 1:
#
#Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
#Output: 13
#
#Example 2:
#
#Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
#Output: 20
#
# 
#
#Constraints:
#
#    2 <= arr1.length == arr2.length <= 40000
#    -10^6 <= arr1[i], arr2[i] <= 10^6
#
#

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        l1, l2 ,l3, l4 = [], [], [], []
        for i in range(len(arr1)):
            l1 += [arr1[i]+arr2[i]+i]
            l2 += [arr1[i]-arr2[i]+i]
            l3 += [-arr1[i]+arr2[i]+i]
            l4 += [-arr1[i]-arr2[i]+i]
        res = []
        res += [max(l1)-min(l1)]
        res += [max(l2) -min(l2)]
        res += [max(l3)-min(l3)]
        res += [max(l4)-min(l4)]
        return max(res)


def maxAbsValExpr(arr1, arr2):
    max1 = max2 = max3 = max4 = float('-inf')
    min1 = min2 = min3 = min4 = float('inf')

    for i in range(len(arr1)):
        tmp1 = arr1[i] - arr2[i] - i
        max1 = max(max1 , tmp1)
        min1 = min(min1 , tmp1)

        tmp2 = arr1[i] + arr2[i] - i
        max2 = max(max2 , tmp2)
        min2 = min(min2 , tmp2)

        tmp3 = arr1[i] + arr2[i] + i
        max3 = max(max3 , tmp3)
        min3 = min(min3 , tmp3)

        
        tmp4 = arr1[i] - arr2[i] + i
        max4 = max(max4 , tmp4)
        min4 = min(min4 , tmp4)
   
    return max((max1 - min1), (max2 - min2),(max3 - min3),(max4 - min4))
