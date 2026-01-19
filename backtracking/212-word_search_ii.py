#212. Word Search II
#Hard
#
#Given an m x n board of characters and a list of strings words, return all words
#on the board.
#
#Each word must be constructed from letters of sequentially adjacent cells, where
#adjacent cells are horizontally or vertically neighboring. The same letter cell
#may not be used more than once in a word.
#
#Example 1:
#Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
#       words = ["oath","pea","eat","rain"]
#Output: ["eat","oath"]
#
#Example 2:
#Input: board = [["a","b"],["c","d"]], words = ["abcb"]
#Output: []
#
#Constraints:
#    m == board.length
#    n == board[i].length
#    1 <= m, n <= 12
#    board[i][j] is a lowercase English letter.
#    1 <= words.length <= 3 * 10^4
#    1 <= words[i].length <= 10
#    words[i] consists of lowercase English letters.
#    All the strings of words are unique.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie from words
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        m, n = len(board), len(board[0])
        result = []

        def backtrack(row, col, parent):
            char = board[row][col]
            curr_node = parent.children.get(char)

            if not curr_node:
                return

            # Check if we found a word
            if curr_node.word:
                result.append(curr_node.word)
                curr_node.word = None  # Avoid duplicates

            # Mark as visited
            board[row][col] = '#'

            # Explore neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and board[new_row][new_col] != '#':
                    backtrack(new_row, new_col, curr_node)

            # Restore cell
            board[row][col] = char

            # Optimization: prune empty branches
            if not curr_node.children:
                del parent.children[char]

        # Start backtracking from each cell
        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    backtrack(i, j, root)

        return result
