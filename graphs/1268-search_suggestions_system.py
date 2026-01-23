#1268. Search Suggestions System
#Medium
#
#You are given an array of strings products and a string searchWord.
#
#Design a system that suggests at most three product names from products after
#each character of searchWord is typed. Suggested products should have common
#prefix with searchWord. If there are more than three products with a common
#prefix return the three lexicographically minimums products.
#
#Return a list of lists of the suggested products after each character of
#searchWord is typed.
#
#Example 1:
#Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
#Output: [["mobile","moneypot","monitor"],
#         ["mobile","moneypot","monitor"],
#         ["mouse","mousepad"],
#         ["mouse","mousepad"],
#         ["mouse","mousepad"]]
#
#Example 2:
#Input: products = ["havana"], searchWord = "havana"
#Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
#
#Example 3:
#Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
#Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
#
#Constraints:
#    1 <= products.length <= 1000
#    1 <= products[i].length <= 3000
#    1 <= sum(products[i].length) <= 2 * 10^4
#    All the strings of products are unique.
#    products[i] consists of lowercase English letters.
#    1 <= searchWord.length <= 1000
#    searchWord consists of lowercase English letters.

from typing import List
import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        Sort products, use binary search for each prefix.
        """
        products.sort()
        result = []
        prefix = ""

        for char in searchWord:
            prefix += char
            # Find first product >= prefix
            idx = bisect.bisect_left(products, prefix)

            suggestions = []
            for i in range(idx, min(idx + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break

            result.append(suggestions)

        return result


class SolutionTrie:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """Trie-based solution"""
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.suggestions = []  # Keep top 3 products

        # Build trie
        root = TrieNode()
        products.sort()

        for product in products:
            node = root
            for char in product:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                if len(node.suggestions) < 3:
                    node.suggestions.append(product)

        # Search
        result = []
        node = root

        for char in searchWord:
            if node and char in node.children:
                node = node.children[char]
                result.append(node.suggestions)
            else:
                node = None
                result.append([])

        return result


class SolutionTwoPointers:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """Two pointers approach"""
        products.sort()
        result = []
        left, right = 0, len(products) - 1

        for i, char in enumerate(searchWord):
            # Narrow down the range
            while left <= right and (len(products[left]) <= i or products[left][i] != char):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] != char):
                right -= 1

            # Get up to 3 suggestions
            suggestions = []
            for j in range(left, min(left + 3, right + 1)):
                suggestions.append(products[j])

            result.append(suggestions)

        return result
