#1640. Check Array Formation Through Concatenation
#Easy
#
#You are given an array of distinct integers arr and an array of integer arrays
#pieces, where the integers in pieces are distinct. Your goal is to form arr by
#concatenating the arrays in pieces in any order. However, you are not allowed
#to reorder the integers in each array pieces[i].
#
#Return true if it is possible to form the array arr from pieces. Otherwise,
#return false.
#
#Example 1:
#Input: arr = [15,88], pieces = [[88],[15]]
#Output: true
#Explanation: Concatenate [15] then [88].
#
#Example 2:
#Input: arr = [49,18,16], pieces = [[16,18,49]]
#Output: false
#Explanation: Even though the numbers match, the order in pieces is wrong.
#
#Example 3:
#Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
#Output: true
#Explanation: Concatenate [91] then [4,64] then [78].
#
#Constraints:
#    1 <= pieces.length <= arr.length <= 100
#    sum(pieces[i].length) == arr.length
#    1 <= pieces[i].length <= arr.length
#    1 <= arr[i], pieces[i][j] <= 100
#    The integers in arr are distinct.
#    The integers in pieces are distinct (i.e., if we flatten pieces it forms a
#    list that is equal to arr sorted).

from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        """
        Map first element of each piece to the piece.
        Iterate through arr and match pieces.
        """
        # Map first element -> piece
        piece_map = {p[0]: p for p in pieces}

        i = 0
        while i < len(arr):
            if arr[i] not in piece_map:
                return False

            piece = piece_map[arr[i]]

            # Check if this piece matches arr[i:i+len(piece)]
            for j, val in enumerate(piece):
                if i + j >= len(arr) or arr[i + j] != val:
                    return False

            i += len(piece)

        return True


class SolutionConcat:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        """
        Sort pieces by their position in arr and concatenate.
        """
        # Find position of each piece's first element in arr
        pos = {val: idx for idx, val in enumerate(arr)}

        # Sort pieces by their position in arr
        sorted_pieces = sorted(pieces, key=lambda p: pos.get(p[0], float('inf')))

        # Concatenate and compare
        result = []
        for piece in sorted_pieces:
            result.extend(piece)

        return result == arr


class SolutionHash:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        """
        Hash-based matching.
        """
        first_to_piece = {}
        for piece in pieces:
            first_to_piece[piece[0]] = piece

        idx = 0
        n = len(arr)

        while idx < n:
            start = arr[idx]
            if start not in first_to_piece:
                return False

            piece = first_to_piece[start]
            for val in piece:
                if idx >= n or arr[idx] != val:
                    return False
                idx += 1

        return True


class SolutionSimple:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        """
        Simple approach: convert to string and check.
        """
        # Map element to piece (as tuple for hashing)
        lookup = {p[0]: p for p in pieces}

        result = []
        for num in arr:
            if num in lookup:
                if not result or result[-1] != lookup[num]:
                    result.append(lookup[num])
            else:
                if result and len(result[-1]) > 1:
                    # Continue with current piece
                    pass
                else:
                    return False

        # Actually, let's just iterate through arr
        i = 0
        while i < len(arr):
            if arr[i] not in lookup:
                return False
            piece = lookup[arr[i]]
            if arr[i:i+len(piece)] != piece:
                return False
            i += len(piece)

        return True
