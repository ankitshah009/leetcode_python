#609. Find Duplicate File in System
#Medium
#
#Given a list paths of directory info, including the directory path, and all the
#files with contents in this directory, return all the duplicate files in the file
#system in terms of their paths. You may return the answer in any order.
#
#A group of duplicate files consists of at least two files that have the same content.
#
#A single directory info string in the input list has the following format:
#"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
#
#Example 1:
#Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
#Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
#
#Example 2:
#Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
#Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
#
#Constraints:
#    1 <= paths.length <= 2 * 10^4
#    1 <= paths[i].length <= 3000
#    1 <= sum(paths[i].length) <= 5 * 10^5
#    paths[i] consist of English letters, digits, '/', '.', '(', ')', and ' '.

from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        """Group files by content"""
        content_to_paths = defaultdict(list)

        for path in paths:
            parts = path.split()
            directory = parts[0]

            for file_info in parts[1:]:
                # Parse "filename(content)"
                paren_idx = file_info.index('(')
                filename = file_info[:paren_idx]
                content = file_info[paren_idx + 1:-1]

                full_path = f"{directory}/{filename}"
                content_to_paths[content].append(full_path)

        # Return only groups with duplicates
        return [paths for paths in content_to_paths.values() if len(paths) > 1]


class SolutionRegex:
    """Using regex for parsing"""

    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        import re

        content_to_paths = defaultdict(list)
        pattern = r'(\S+)\(([^)]+)\)'

        for path in paths:
            parts = path.split()
            directory = parts[0]

            for file_info in parts[1:]:
                match = re.match(pattern, file_info)
                if match:
                    filename = match.group(1)
                    content = match.group(2)
                    content_to_paths[content].append(f"{directory}/{filename}")

        return [paths for paths in content_to_paths.values() if len(paths) > 1]
