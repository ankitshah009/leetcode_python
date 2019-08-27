#39. Combination Sum
#Medium
#
#Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
#The same repeated number may be chosen from candidates unlimited number of times.
#
#Note:
#
#    All numbers (including target) will be positive integers.
#    The solution set must not contain duplicate combinations.
#
#Example 1:
#
#Input: candidates = [2,3,6,7], target = 7,
#A solution set is:
#[
#  [7],
#  [2,2,3]
#]
#
#Example 2:
#
#Input: candidates = [2,3,5], target = 8,
#A solution set is:
#[
#  [2,2,2,2],
#  [2,3,3],
#  [3,5]
#]
#
#

class Solution:

    def dfs(self, start, candidates, target, res, path):
        
        if sum(path) == target:
            res.append(path[:])
        
        for i in range(start, len(candidates)):
            if (sum(path) + candidates[i]) > target:
                break
            path.append(candidates[i])
            self.dfs(i, candidates, target, res, path)
            path.remove(path[-1])
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:    
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
    
        if not candidates:
            return res
        
        candidates =  sorted(candidates)
        start = 0
        self.dfs(start, candidates, target, res, path)
	return res
