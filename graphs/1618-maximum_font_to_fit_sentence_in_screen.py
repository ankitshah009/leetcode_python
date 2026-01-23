#1618. Maximum Font to Fit a Sentence in a Screen
#Medium
#
#You are given a string text. We want to display text on a screen of width w
#and height h. You can choose any font size from array fonts, which contains
#the available font sizes in ascending order.
#
#You can use the FontInfo interface to get the width and height of any character
#at any available font size.
#
#The FontInfo interface is defined as such:
#
#interface FontInfo {
#  // Returns the width of character ch on the screen using font size fontSize.
#  // O(1) per call
#  public int getWidth(int fontSize, char ch);
#
#  // Returns the height of any character on the screen using font size fontSize.
#  // O(1) per call
#  public int getHeight(int fontSize);
#}
#
#The calculated width of text for some fontSize is the sum of every
#getWidth(fontSize, text[i]) call for each 0 <= i < text.length (0-indexed).
#The calculated height of text for some fontSize is getHeight(fontSize).
#Note that text is displayed on a single line.
#
#It is guaranteed that FontInfo will return the same value if you call
#getHeight or getWidth with the same parameters.
#
#It is also guaranteed that for any font size fontSize and any character ch:
#- getHeight(fontSize) <= getHeight(fontSize+1)
#- getWidth(fontSize, ch) <= getWidth(fontSize+1, ch)
#
#Return the maximum font size you can use to display text on the screen.
#If text cannot fit on the display with any font size, return -1.
#
#Example 1:
#Input: text = "helloworld", w = 80, h = 20, fonts = [6,8,10,12,14,16,18,24,36]
#Output: 6
#
#Example 2:
#Input: text = "leetcode", w = 1000, h = 50, fonts = [1,2,4]
#Output: 4
#
#Example 3:
#Input: text = "easyquestion", w = 100, h = 100, fonts = [10,15,20,25]
#Output: -1
#
#Constraints:
#    1 <= text.length <= 50000
#    text contains only lowercase English letters.
#    1 <= w <= 10^7
#    1 <= h <= 10^4
#    1 <= fonts.length <= 10^5
#    1 <= fonts[i] <= 10^5
#    fonts is sorted in ascending order and does not contain duplicates.

from typing import List

# FontInfo interface definition
class FontInfo:
    def getWidth(self, fontSize: int, ch: str) -> int:
        pass

    def getHeight(self, fontSize: int) -> int:
        pass


class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo: 'FontInfo') -> int:
        """
        Binary search for the maximum font size that fits.
        """
        def fits(fontSize: int) -> bool:
            # Check height first (faster)
            if fontInfo.getHeight(fontSize) > h:
                return False

            # Calculate total width
            total_width = sum(fontInfo.getWidth(fontSize, ch) for ch in text)
            return total_width <= w

        # Binary search for largest font that fits
        left, right = 0, len(fonts) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if fits(fonts[mid]):
                result = fonts[mid]
                left = mid + 1  # Try larger
            else:
                right = mid - 1  # Try smaller

        return result


class SolutionOptimized:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo: 'FontInfo') -> int:
        """
        Optimized with early termination and character caching.
        """
        from collections import Counter

        # Count character frequencies for faster width calculation
        char_count = Counter(text)

        def fits(fontSize: int) -> bool:
            if fontInfo.getHeight(fontSize) > h:
                return False

            total_width = 0
            for ch, count in char_count.items():
                total_width += fontInfo.getWidth(fontSize, ch) * count
                if total_width > w:
                    return False

            return True

        # Binary search
        lo, hi = 0, len(fonts) - 1
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if fits(fonts[mid]):
                ans = fonts[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans


class SolutionLinear:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo: 'FontInfo') -> int:
        """
        Linear search from largest to smallest (less efficient but simpler).
        """
        for fontSize in reversed(fonts):
            # Check height
            if fontInfo.getHeight(fontSize) > h:
                continue

            # Check width
            total_width = sum(fontInfo.getWidth(fontSize, ch) for ch in text)
            if total_width <= w:
                return fontSize

        return -1
