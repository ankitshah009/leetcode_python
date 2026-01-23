#846. Hand of Straights
#Medium
#
#Alice has some number of cards and she wants to rearrange the cards into groups
#so that each group is of size groupSize, and consists of groupSize consecutive cards.
#
#Given an integer array hand where hand[i] is the value written on the ith card
#and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
#
#Example 1:
#Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
#Output: true
#Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
#
#Example 2:
#Input: hand = [1,2,3,4,5], groupSize = 4
#Output: false
#Explanation: Alice's hand can not be rearranged into groups of 4.
#
#Constraints:
#    1 <= hand.length <= 10^4
#    0 <= hand[i] <= 10^9
#    1 <= groupSize <= hand.length

from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        """
        Greedy: always form group starting from smallest available card.
        """
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        sorted_keys = sorted(count.keys())

        for start in sorted_keys:
            if count[start] > 0:
                need = count[start]

                # Try to form 'need' groups starting from 'start'
                for card in range(start, start + groupSize):
                    if count[card] < need:
                        return False
                    count[card] -= need

        return True


class SolutionDeque:
    """Using deque for tracking groups"""

    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        from collections import deque

        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        sorted_keys = sorted(count.keys())

        # groups[i] = number of groups needing card (current + i)
        groups = deque()
        open_groups = 0
        last_card = -1

        for card in sorted_keys:
            # Close groups that can't continue
            if groups and card > last_card + 1:
                if open_groups > 0:
                    return False
                groups.clear()
                open_groups = 0

            # Check if we have enough cards
            if count[card] < open_groups:
                return False

            # Start new groups
            new_groups = count[card] - open_groups
            groups.append(new_groups)
            open_groups = count[card]

            # Complete groups
            if len(groups) == groupSize:
                open_groups -= groups.popleft()

            last_card = card

        return open_groups == 0


class SolutionSimple:
    """Simpler greedy"""

    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for card in sorted(count):
            while count[card] > 0:
                for i in range(groupSize):
                    if count[card + i] <= 0:
                        return False
                    count[card + i] -= 1

        return True
