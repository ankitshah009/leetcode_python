#765. Couples Holding Hands
#Hard
#
#There are n couples sitting in 2n seats arranged in a row and want to hold
#hands.
#
#The people and seats are represented by an integer array row where row[i] is
#the ID of the person sitting in the ith seat. The couples are numbered in
#order, the first couple being (0, 1), the second couple being (2, 3), and so
#on with the last couple being (2n - 2, 2n - 1).
#
#Return the minimum number of swaps so that every couple is sitting side by side.
#A swap consists of choosing any two people, then they stand up and switch seats.
#
#Example 1:
#Input: row = [0,2,1,3]
#Output: 1
#Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
#
#Example 2:
#Input: row = [3,2,0,1]
#Output: 0
#Explanation: All couples are already seated side by side.
#
#Constraints:
#    2n == row.length
#    2 <= n <= 30
#    n is even.
#    0 <= row[i] < 2n
#    All the elements of row are unique.

class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        """
        Greedy: for each couch, if couple not together, swap partner in.
        """
        n = len(row)
        pos = {person: i for i, person in enumerate(row)}

        swaps = 0

        for i in range(0, n, 2):
            person = row[i]
            partner = person ^ 1  # Partner of person p is p^1

            if row[i + 1] != partner:
                # Find partner and swap
                partner_pos = pos[partner]

                # Swap row[i + 1] and row[partner_pos]
                other = row[i + 1]
                row[i + 1], row[partner_pos] = row[partner_pos], row[i + 1]
                pos[other], pos[partner] = partner_pos, i + 1

                swaps += 1

        return swaps


class SolutionUnionFind:
    """Union-Find: count cycles of misplaced couples"""

    def minSwapsCouples(self, row: list[int]) -> int:
        n = len(row) // 2
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                return True
            return False

        # Union couples sitting on same couch
        for i in range(n):
            couple1 = row[2 * i] // 2
            couple2 = row[2 * i + 1] // 2
            union(couple1, couple2)

        # Count number of components (cycles)
        # Swaps needed = n - number of components
        components = sum(1 for i in range(n) if find(i) == i)
        return n - components


class SolutionCycleCount:
    """Direct cycle counting"""

    def minSwapsCouples(self, row: list[int]) -> int:
        n = len(row)
        pos = {person: i for i, person in enumerate(row)}

        swaps = 0
        visited = [False] * (n // 2)

        for couch in range(n // 2):
            if visited[couch]:
                continue

            # Follow the cycle
            cycle_length = 0
            curr = couch

            while not visited[curr]:
                visited[curr] = True
                cycle_length += 1

                # Find which couch has the partner of first person on curr couch
                person1 = row[2 * curr]
                partner1 = person1 ^ 1
                partner1_couch = pos[partner1] // 2

                if not visited[partner1_couch]:
                    curr = partner1_couch
                else:
                    break

            swaps += cycle_length - 1

        return swaps
