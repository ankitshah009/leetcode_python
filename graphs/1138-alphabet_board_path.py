#1138. Alphabet Board Path
#Medium
#
#On an alphabet board, we start at position (0, 0), corresponding to character
#board[0][0].
#
#Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown
#in the diagram below.
#
#We may make the following moves:
#    'U' moves our position up one row, if the position exists on the board;
#    'D' moves our position down one row, if the position exists on the board;
#    'L' moves our position left one column, if the position exists on the board;
#    'R' moves our position right one column, if the position exists on the board;
#    '!' adds the character board[r][c] at our current position (r, c) to the answer.
#
#Return a sequence of moves that makes our answer equal to target in the
#minimum number of moves. You may return any path that does so.
#
#Example 1:
#Input: target = "leet"
#Output: "DDR!UURRR!!DDD!"
#
#Example 2:
#Input: target = "code"
#Output: "RR!DDRR!UUL!R!"
#
#Constraints:
#    1 <= target.length <= 100
#    target consists only of English lowercase letters.

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        """
        Calculate path from current position to target letter.
        Handle 'z' specially (only accessible from above).
        """
        def get_pos(c):
            idx = ord(c) - ord('a')
            return idx // 5, idx % 5

        result = []
        curr_r, curr_c = 0, 0

        for c in target:
            target_r, target_c = get_pos(c)

            # Move up/left before down/right (to handle 'z' at (5,0))
            if target_r < curr_r:
                result.append('U' * (curr_r - target_r))
            if target_c < curr_c:
                result.append('L' * (curr_c - target_c))
            if target_r > curr_r:
                result.append('D' * (target_r - curr_r))
            if target_c > curr_c:
                result.append('R' * (target_c - curr_c))

            result.append('!')
            curr_r, curr_c = target_r, target_c

        return ''.join(result)


class SolutionAlternative:
    def alphabetBoardPath(self, target: str) -> str:
        """Handle z by always moving up/left first"""
        result = []
        r, c = 0, 0

        for char in target:
            idx = ord(char) - ord('a')
            tr, tc = idx // 5, idx % 5

            # Order: U, L, D, R to avoid going out of bounds at 'z'
            while r > tr:
                result.append('U')
                r -= 1
            while c > tc:
                result.append('L')
                c -= 1
            while r < tr:
                result.append('D')
                r += 1
            while c < tc:
                result.append('R')
                c += 1

            result.append('!')

        return ''.join(result)
