#1233. Remove Sub-Folders from the Filesystem
#Medium
#
#Given a list of folders folder, return the folders after removing all
#sub-folders in those folders. You may return the answer in any order.
#
#If a folder[i] is located within another folder[j], it is called a sub-folder of it.
#
#The format of a path is one or more concatenated strings of the form: '/'
#followed by one or more lowercase English letters.
#
#Example 1:
#Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
#Output: ["/a","/c/d","/c/f"]
#Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of
#folder "/c/d" in our filesystem.
#
#Example 2:
#Input: folder = ["/a","/a/b/c","/a/b/d"]
#Output: ["/a"]
#Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are
#subfolders of "/a".
#
#Example 3:
#Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
#Output: ["/a/b/c","/a/b/ca","/a/b/d"]
#
#Constraints:
#    1 <= folder.length <= 4 * 10^4
#    2 <= folder[i].length <= 100
#    folder[i] contains only lowercase letters and '/'.
#    folder[i] always starts with the character '/'.
#    Each folder name is unique.

from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[int]:
        """
        Sort folders. After sorting, a subfolder will always come right
        after its parent folder.
        """
        folder.sort()
        result = [folder[0]]

        for i in range(1, len(folder)):
            # Check if current is subfolder of last added
            parent = result[-1]
            # Must start with parent + '/' to be a subfolder
            if not folder[i].startswith(parent + '/'):
                result.append(folder[i])

        return result


class SolutionSet:
    def removeSubfolders(self, folder: List[str]) -> List[int]:
        """Using set for quick lookup"""
        folder_set = set(folder)
        result = []

        for f in folder:
            is_subfolder = False
            # Check all prefixes
            for i in range(1, len(f)):
                if f[i] == '/' and f[:i] in folder_set:
                    is_subfolder = True
                    break

            if not is_subfolder:
                result.append(f)

        return result


class SolutionTrie:
    def removeSubfolders(self, folder: List[str]) -> List[int]:
        """Using Trie"""
        trie = {}

        # Build trie
        for f in folder:
            node = trie
            for part in f.split('/')[1:]:  # Skip empty string before first /
                if part not in node:
                    node[part] = {}
                node = node[part]
            node['#'] = f  # Mark end of folder

        # DFS to collect non-subfolders
        result = []

        def dfs(node):
            if '#' in node:
                result.append(node['#'])
                return  # Don't go deeper (subfolders)

            for key in node:
                if key != '#':
                    dfs(node[key])

        dfs(trie)
        return result
