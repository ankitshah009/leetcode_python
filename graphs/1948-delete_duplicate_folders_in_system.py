#1948. Delete Duplicate Folders in System
#Hard
#
#Due to a bug, there are many duplicate folders in a file system. You are given
#a 2D array paths, where paths[i] is an array representing an absolute path to
#the ith folder in the file system.
#
#Two folders (not necessarily on the same level) are identical if they contain
#the same non-empty set of identical subfolders and underlying subfolder
#structure. The folders do not need to be at the root level to be identical. If
#two or more folders are identical, then mark the folders as well as all their
#subfolders.
#
#Once all folders to be deleted have been marked, the file system will delete
#all of them. The file system only runs the deletion once, so any folders that
#become identical after the initial deletion are not deleted.
#
#Return the 2D array ans containing the paths of the remaining folders after
#deleting all the marked folders. The paths may be returned in any order.
#
#Example 1:
#Input: paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
#Output: [["d"],["d","a"]]
#
#Constraints:
#    1 <= paths.length <= 2 * 10^4
#    1 <= paths[i].length <= 500
#    1 <= paths[i][j].length <= 10
#    1 <= sum(paths[i][j].length) <= 2 * 10^5
#    paths[i][j] consists of lowercase English letters.
#    No two paths lead to the same folder.
#    For any folder not at the root level, its parent folder is also in paths.

from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[int]]:
        """
        Build trie, serialize subtrees, mark duplicates, collect remaining.
        """
        root = TrieNode()

        # Build trie
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode()
                node = node.children[folder]

        # Serialize subtrees and find duplicates
        serializations = defaultdict(list)

        def serialize(node: TrieNode) -> str:
            if not node.children:
                return ""

            parts = []
            for name in sorted(node.children):
                child_serial = serialize(node.children[name])
                parts.append(f"({name}{child_serial})")

            serial = ''.join(parts)
            serializations[serial].append(node)
            return serial

        serialize(root)

        # Mark duplicates for deletion
        for serial, nodes in serializations.items():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        # Collect remaining paths
        result = []

        def collect(node: TrieNode, path: list):
            for name, child in node.children.items():
                if not child.deleted:
                    path.append(name)
                    result.append(path[:])
                    collect(child, path)
                    path.pop()

        collect(root, [])
        return result


class SolutionDetailed:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        """
        Same approach with clearer structure.
        """
        # Build trie
        root = {}

        for path in paths:
            node = root
            for folder in path:
                node = node.setdefault(folder, {})

        # Serialize and track duplicates
        seen = {}
        duplicates = set()

        def build_serial(node):
            if not node:
                return ""

            serial_parts = []
            for name in sorted(node):
                child_serial = build_serial(node[name])
                serial_parts.append(f"({name}{child_serial})")

            serial = ''.join(serial_parts)

            if serial:
                if serial in seen:
                    duplicates.add(id(seen[serial]))
                    duplicates.add(id(node))
                else:
                    seen[serial] = node

            return serial

        build_serial(root)

        # Collect non-deleted paths
        result = []

        def dfs(node, path):
            for name in node:
                child = node[name]
                if id(child) not in duplicates:
                    new_path = path + [name]
                    result.append(new_path)
                    dfs(child, new_path)

        dfs(root, [])
        return result
