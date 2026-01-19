#514. Freedom Trail
#Hard
#
#In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal
#dial called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open
#the door.
#
#Given a string ring that represents the code engraved on the outer ring and another string
#key that represents the keyword that needs to be spelled, return the minimum number of steps
#to spell all the characters in the keyword.
#
#Initially, the first character of the ring is aligned at the "12:00" direction. You should
#spell all the characters in key one by one by rotating ring clockwise or anticlockwise to
#make each character of the string key aligned at the "12:00" direction and then by pressing
#the center button.
#
#At the stage of rotating the ring to spell the key character key[i]:
#    You can rotate the ring clockwise or anticlockwise by one place, which counts as one step.
#        The final purpose of the rotation is to align one of ring's characters at the "12:00"
#        direction, where this character must equal key[i].
#    If the character key[i] has been aligned at the "12:00" direction, press the center
#        button to spell, which also counts as one step. After the pressing, you could begin
#        to spell the next character in the key (next stage). Otherwise, you've finished all
#        the spelling.
#
#Example 1:
#Input: ring = "godding", key = "gd"
#Output: 4
#Explanation:
#For the first key character 'g', since it is already in place, we just need 1 step to spell it.
#For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two
#steps to make it become "ddinggo".
#Also, we need 1 more step for spelling.
#So the final output is 4.
#
#Example 2:
#Input: ring = "godding", key = "godding"
#Output: 13
#
#Constraints:
#    1 <= ring.length, key.length <= 100
#    ring and key consist of only lower case English letters.
#    It is guaranteed that key could always be spelled by rotating ring.

from functools import lru_cache
from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)

        # Build index map: character -> list of positions
        char_pos = defaultdict(list)
        for i, c in enumerate(ring):
            char_pos[c].append(i)

        @lru_cache(maxsize=None)
        def dp(ring_pos, key_idx):
            if key_idx == len(key):
                return 0

            min_steps = float('inf')
            char = key[key_idx]

            for next_pos in char_pos[char]:
                # Calculate minimum rotation distance
                clockwise = abs(next_pos - ring_pos)
                counter_clockwise = n - clockwise
                rotation = min(clockwise, counter_clockwise)

                # +1 for pressing the button
                steps = rotation + 1 + dp(next_pos, key_idx + 1)
                min_steps = min(min_steps, steps)

            return min_steps

        return dp(0, 0)
