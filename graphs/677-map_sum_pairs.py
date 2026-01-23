#677. Map Sum Pairs
#Medium
#
#Design a map that allows you to do the following:
#- Maps a string key to a given value.
#- Returns the sum of the values that have a key with a prefix equal to a given string.
#
#Implement the MapSum class:
#- MapSum() Initializes the MapSum object.
#- void insert(String key, int val) Inserts the key-val pair into the map. If the
#  key already existed, the original key-value pair will be overridden to the new one.
#- int sum(String prefix) Returns the sum of all the pairs' value whose key starts
#  with the prefix.
#
#Example 1:
#Input: ["MapSum", "insert", "sum", "insert", "sum"]
#       [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
#Output: [null, null, 3, null, 5]
#
#Constraints:
#    1 <= key.length, prefix.length <= 50
#    key and prefix consist of only lowercase English letters.
#    1 <= val <= 1000
#    At most 50 calls will be made to insert and sum.

class MapSum:
    """
    Trie-based implementation.
    Store value at each node and update along the path.
    """

    def __init__(self):
        self.trie = {}
        self.map = {}  # Store original values for updates

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val

        node = self.trie
        for c in key:
            if c not in node:
                node[c] = {'_sum': 0}
            node = node[c]
            node['_sum'] += delta

    def sum(self, prefix: str) -> int:
        node = self.trie
        for c in prefix:
            if c not in node:
                return 0
            node = node[c]
        return node['_sum']


class MapSumBruteForce:
    """Simple hash map solution"""

    def __init__(self):
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        total = 0
        for key, val in self.map.items():
            if key.startswith(prefix):
                total += val
        return total


class MapSumTrieAlt:
    """Trie with DFS for sum"""

    def __init__(self):
        self.trie = {}
        self.values = {}

    def insert(self, key: str, val: int) -> None:
        self.values[key] = val

        node = self.trie
        for c in key:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = key  # Store key reference

    def sum(self, prefix: str) -> int:
        # Navigate to prefix node
        node = self.trie
        for c in prefix:
            if c not in node:
                return 0
            node = node[c]

        # DFS to collect all keys under this prefix
        def dfs(node):
            total = 0
            if '$' in node:
                total += self.values[node['$']]
            for c in node:
                if c != '$':
                    total += dfs(node[c])
            return total

        return dfs(node)
