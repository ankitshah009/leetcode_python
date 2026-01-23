#1452. People Whose List of Favorite Companies Is Not a Subset of Another List
#Medium
#
#Given the array favoriteCompanies where favoriteCompanies[i] is the list of
#favorites companies for the ith person (indexed from 0).
#
#Return the indices of people whose list of favorite companies is not a subset
#of any other list of favorites companies. You must return the indices in
#increasing order.
#
#Example 1:
#Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
#Output: [0,1,4]
#Explanation:
#Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a
#subset of favoriteCompanies[0]=["leetcode","google","facebook"] corresponding
#to the person with index 0.
#Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of
#favoriteCompanies[0]=["leetcode","google","facebook"] and favoriteCompanies[1]=["google","microsoft"].
#Other lists of favorite companies are not a subset of another list, therefore,
#the answer is [0,1,4].
#
#Example 2:
#Input: favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
#Output: [0,1]
#Explanation: In this case favoriteCompanies[2]=["facebook","google"] is a subset
#of favoriteCompanies[0]=["leetcode","google","facebook"], therefore, the answer is [0,1].
#
#Example 3:
#Input: favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
#Output: [0,1,2,3]
#
#Constraints:
#    1 <= favoriteCompanies.length <= 100
#    1 <= favoriteCompanies[i].length <= 500
#    1 <= favoriteCompanies[i][j].length <= 20
#    All strings in favoriteCompanies[i] are distinct.
#    All lists of favorite companies are distinct, that is, If we sort
#    alphabetically each list then favoriteCompanies[i] != favoriteCompanies[j].
#    All strings consist of lowercase English letters only.

from typing import List

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        """
        Convert each list to set. For each set, check if it's a subset of any other.
        O(n^2 * m) where n = number of people, m = max companies per person.
        """
        n = len(favoriteCompanies)
        company_sets = [set(companies) for companies in favoriteCompanies]

        result = []

        for i in range(n):
            is_subset = False
            for j in range(n):
                if i != j and len(company_sets[i]) < len(company_sets[j]):
                    if company_sets[i].issubset(company_sets[j]):
                        is_subset = True
                        break

            if not is_subset:
                result.append(i)

        return result


class SolutionSorted:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        """
        Sort by set size descending. A set can only be subset of larger sets.
        """
        n = len(favoriteCompanies)
        company_sets = [set(companies) for companies in favoriteCompanies]

        # Sort indices by set size (descending)
        indices_by_size = sorted(range(n), key=lambda i: -len(company_sets[i]))

        result = []

        for idx in range(n):
            i = indices_by_size[idx]
            is_subset = False

            # Only check against larger sets (which come before in sorted order)
            for prev_idx in range(idx):
                j = indices_by_size[prev_idx]
                if company_sets[i].issubset(company_sets[j]):
                    is_subset = True
                    break

            if not is_subset:
                result.append(i)

        return sorted(result)


class SolutionHashing:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        """Using frozenset for hashing"""
        n = len(favoriteCompanies)
        company_sets = [frozenset(companies) for companies in favoriteCompanies]

        result = []

        for i in range(n):
            is_subset = False
            for j in range(n):
                if i != j and len(company_sets[i]) <= len(company_sets[j]):
                    if company_sets[i] <= company_sets[j]:
                        is_subset = True
                        break

            if not is_subset:
                result.append(i)

        return result
