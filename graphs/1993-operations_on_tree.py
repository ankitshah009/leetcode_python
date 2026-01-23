#1993. Operations on Tree
#Medium
#
#You are given a tree with n nodes numbered from 0 to n - 1 in the form of a
#parent array parent, where parent[i] is the parent of the ith node. The root
#of the tree is node 0, so parent[0] = -1 since it has no parent. You want to
#design a data structure that allows users to lock, unlock, and upgrade nodes
#in the tree.
#
#The data structure should support the following functions:
#- Lock: Locks the given node for the given user and prevents other users from
#  locking the same node. You may only lock a node if it is unlocked.
#- Unlock: Unlocks the given node for the given user. You may only unlock a
#  node if it is currently locked by the same user.
#- Upgrade: Locks the given node for the given user and unlocks all of its
#  descendants regardless of who locked it. You may only upgrade a node if all
#  3 conditions are met:
#  - The node is unlocked,
#  - It has at least one locked descendant (by any user), and
#  - It does not have any locked ancestors.
#
#Example:
#Input: ["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
#       [[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
#Output: [null, true, false, true, true, true, false]
#
#Constraints:
#    n == parent.length
#    2 <= n <= 2000
#    0 <= parent[i] <= n - 1 for i != 0
#    parent[0] == -1
#    0 <= num <= n - 1
#    1 <= user <= 10^4
#    parent represents a valid tree.
#    At most 2000 calls in total will be made to lock, unlock, and upgrade.

from typing import List
from collections import defaultdict

class LockingTree:
    def __init__(self, parent: List[int]):
        self.parent = parent
        self.n = len(parent)
        self.locked = {}  # node -> user who locked it
        self.children = defaultdict(list)

        for i in range(1, self.n):
            self.children[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        """Lock node if unlocked."""
        if num in self.locked:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        """Unlock node if locked by same user."""
        if num not in self.locked or self.locked[num] != user:
            return False
        del self.locked[num]
        return True

    def upgrade(self, num: int, user: int) -> bool:
        """
        Lock node and unlock all descendants if:
        1. Node is unlocked
        2. Has at least one locked descendant
        3. Has no locked ancestors
        """
        # Check if node is unlocked
        if num in self.locked:
            return False

        # Check for locked ancestors
        curr = self.parent[num]
        while curr != -1:
            if curr in self.locked:
                return False
            curr = self.parent[curr]

        # Find and unlock all locked descendants
        locked_descendants = []
        self._find_locked_descendants(num, locked_descendants)

        if not locked_descendants:
            return False

        # Unlock all descendants
        for node in locked_descendants:
            del self.locked[node]

        # Lock the current node
        self.locked[num] = user
        return True

    def _find_locked_descendants(self, node: int, result: List[int]):
        """DFS to find all locked descendants."""
        for child in self.children[node]:
            if child in self.locked:
                result.append(child)
            self._find_locked_descendants(child, result)


class LockingTreeOptimized:
    """
    Same logic with slight optimization for ancestor checking.
    """
    def __init__(self, parent: List[int]):
        self.parent = parent
        self.n = len(parent)
        self.locked = {}
        self.children = defaultdict(list)

        for i in range(1, self.n):
            self.children[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked.get(num) != user:
            return False
        del self.locked[num]
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False

        # Check ancestors
        curr = self.parent[num]
        while curr != -1:
            if curr in self.locked:
                return False
            curr = self.parent[curr]

        # Find locked descendants using iterative DFS
        locked_descendants = []
        stack = list(self.children[num])

        while stack:
            node = stack.pop()
            if node in self.locked:
                locked_descendants.append(node)
            stack.extend(self.children[node])

        if not locked_descendants:
            return False

        for node in locked_descendants:
            del self.locked[node]

        self.locked[num] = user
        return True
