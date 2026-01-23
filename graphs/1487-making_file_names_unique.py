#1487. Making File Names Unique
#Medium
#
#Given an array of strings names of size n. You will create n folders in your
#file system such that, at the ith minute, you will create a folder with the
#name names[i].
#
#Since two files cannot have the same name, if you enter a folder name that was
#previously used, the system will have a suffix addition to its name in the
#form of (k), where, k is the smallest positive integer such that the obtained
#name remains unique.
#
#Return an array of strings of length n where ans[i] is the actual name the
#system will assign to the ith folder when you create it.
#
#Example 1:
#Input: names = ["gy","a","x","gy","gy","gy"]
#Output: ["gy","a","x","gy(1)","gy(2)","gy(3)"]
#
#Example 2:
#Input: names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
#Output: ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
#Explanation: When the last folder is created, the smallest positive valid k is 4.
#
#Example 3:
#Input: names = ["wano","wano","wano","wano"]
#Output: ["wano","wano(1)","wano(2)","wano(3)"]
#
#Example 4:
#Input: names = ["kaido","kaido(1)","kaido","kaido(1)"]
#Output: ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
#
#Constraints:
#    1 <= names.length <= 5 * 10^4
#    1 <= names[i].length <= 20
#    names[i] consists of lowercase English letters, digits, and/or round brackets.

from typing import List

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        """
        Track used names and next available suffix for each base name.
        """
        used = set()  # Set of used names
        next_suffix = {}  # base_name -> next suffix to try

        result = []

        for name in names:
            if name not in used:
                # Name is available
                used.add(name)
                result.append(name)
                next_suffix[name] = 1
            else:
                # Need to find unique suffix
                k = next_suffix.get(name, 1)

                # Find smallest valid k
                new_name = f"{name}({k})"
                while new_name in used:
                    k += 1
                    new_name = f"{name}({k})"

                used.add(new_name)
                result.append(new_name)

                # Update next suffix for both base name and new name
                next_suffix[name] = k + 1
                next_suffix[new_name] = 1

        return result


class SolutionOptimized:
    def getFolderNames(self, names: List[str]) -> List[str]:
        """
        Optimized: only track next suffix, check membership in suffix dict.
        """
        # name -> next k to try
        name_count = {}
        result = []

        for name in names:
            if name not in name_count:
                # First occurrence
                result.append(name)
                name_count[name] = 1
            else:
                # Find unique suffix
                k = name_count[name]
                new_name = f"{name}({k})"

                while new_name in name_count:
                    k += 1
                    new_name = f"{name}({k})"

                result.append(new_name)
                name_count[name] = k + 1
                name_count[new_name] = 1

        return result


class SolutionAlternative:
    def getFolderNames(self, names: List[str]) -> List[str]:
        """Alternative implementation with cleaner logic"""
        used = {}  # name -> next available suffix

        result = []
        for name in names:
            if name not in used:
                final_name = name
            else:
                k = used[name]
                final_name = f"{name}({k})"
                while final_name in used:
                    k += 1
                    final_name = f"{name}({k})"
                used[name] = k + 1

            result.append(final_name)
            used[final_name] = 1

        return result
