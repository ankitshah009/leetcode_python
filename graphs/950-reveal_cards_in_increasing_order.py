#950. Reveal Cards In Increasing Order
#Medium
#
#You are given an integer array deck. There is a deck of cards where every card
#has a unique integer.
#
#You want to order the deck of cards such that when the cards are revealed one
#by one, they are revealed in increasing order.
#
#The revealing process is:
#1. Take the top card of the deck, reveal it, and take it out of the deck.
#2. If there are still cards in the deck, put the next top card of the deck at
#   the bottom of the deck.
#3. Repeat until all cards are revealed.
#
#Return an ordering of the deck that would reveal the cards in increasing order.
#
#Example 1:
#Input: deck = [17,13,11,2,3,5,7]
#Output: [2,13,3,11,5,17,7]
#
#Example 2:
#Input: deck = [1,1000]
#Output: [1,1000]
#
#Constraints:
#    1 <= deck.length <= 1000
#    1 <= deck[i] <= 10^6
#    All the values of deck are unique.

from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        """
        Simulate in reverse: work backwards from sorted deck.
        """
        deck.sort(reverse=True)
        result = deque()

        for card in deck:
            if result:
                # Reverse of putting top to bottom: move bottom to top
                result.appendleft(result.pop())
            result.appendleft(card)

        return list(result)


class SolutionIndices:
    """Track indices using simulation"""

    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        n = len(deck)
        deck.sort()

        # Simulate to get order of indices
        indices = deque(range(n))
        result = [0] * n

        for card in deck:
            # Take top index
            idx = indices.popleft()
            result[idx] = card

            # Move next index to bottom
            if indices:
                indices.append(indices.popleft())

        return result


class SolutionSimulate:
    """Forward simulation to find positions"""

    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        n = len(deck)
        deck.sort()

        # Find the order in which positions are revealed
        positions = deque(range(n))
        reveal_order = []

        while positions:
            reveal_order.append(positions.popleft())
            if positions:
                positions.append(positions.popleft())

        # Place sorted cards in reveal order
        result = [0] * n
        for i, pos in enumerate(reveal_order):
            result[pos] = deck[i]

        return result
