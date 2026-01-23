#800. Similar RGB Color
#Easy (Premium)
#
#The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.
#For example, "#15c" is shorthand for the color "#1155cc".
#
#The similarity between the two colors "#ABCDEF" and "#UVWXYZ" is
#-(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.
#
#Given a string color that follows the format "#ABCDEF", return a string
#represents the color that is most similar to the given color and has a
#shorthand (i.e., it can be represented as some "#XYZ").
#
#Any answer which has the same highest similarity as the best answer will be
#accepted.
#
#Example 1:
#Input: color = "#09f166"
#Output: "#11ee66"
#Explanation: The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2
#= -64 -9 -0 = -73.
#This is the highest among any shorthand color.
#
#Example 2:
#Input: color = "#4e3fe1"
#Output: "#5544dd"
#
#Constraints:
#    color.length == 7
#    color[0] == '#'
#    color[i] is either digit or character in the range ['a', 'f'] for i > 0.

class Solution:
    def similarRGB(self, color: str) -> str:
        """
        For each component, find closest shorthand value.
        Shorthand values: 00, 11, 22, ..., ff (0, 17, 34, ..., 255)
        """
        def closest_shorthand(hex_val):
            """Find closest shorthand value to hex_val (0-255)"""
            # Shorthand values are 0x00, 0x11, 0x22, ..., 0xff
            # These are 0, 17, 34, 51, ..., 255 (multiples of 17)
            # Find closest multiple of 17
            q = round(hex_val / 17)
            val = q * 17
            # Convert to two-char hex
            hex_char = format(q, 'x')
            return hex_char * 2

        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)

        return '#' + closest_shorthand(r) + closest_shorthand(g) + closest_shorthand(b)


class SolutionBruteForce:
    """Try all shorthand colors"""

    def similarRGB(self, color: str) -> str:
        def similarity(c1, c2):
            r1, g1, b1 = int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16)
            r2, g2, b2 = int(c2[1:3], 16), int(c2[3:5], 16), int(c2[5:7], 16)
            return -(r1-r2)**2 - (g1-g2)**2 - (b1-b2)**2

        hex_chars = '0123456789abcdef'
        best_color = None
        best_sim = float('-inf')

        for r in hex_chars:
            for g in hex_chars:
                for b in hex_chars:
                    shorthand = f'#{r}{r}{g}{g}{b}{b}'
                    sim = similarity(color, shorthand)
                    if sim > best_sim:
                        best_sim = sim
                        best_color = shorthand

        return best_color


class SolutionMath:
    """Mathematical approach"""

    def similarRGB(self, color: str) -> str:
        result = '#'

        for i in range(1, 7, 2):
            val = int(color[i:i+2], 16)
            # Find closest from {0, 17, 34, ..., 255}
            # Round to nearest 17
            idx = (val + 8) // 17  # +8 for proper rounding
            idx = min(15, max(0, idx))  # Clamp to valid range
            result += format(idx, 'x') * 2

        return result
