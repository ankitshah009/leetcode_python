#271. Encode and Decode Strings
#Medium
#
#Design an algorithm to encode a list of strings to a string. The encoded string
#is then sent over the network and is decoded back to the original list of strings.
#
#Please implement encode and decode
#
#Example 1:
#Input: dummy_input = ["Hello","World"]
#Output: ["Hello","World"]
#Explanation:
#Codec codec = new Codec();
#codec.decode(codec.encode(strs)) returns the same string list
#
#Example 2:
#Input: dummy_input = [""]
#Output: [""]
#
#Constraints:
#    1 <= strs.length <= 200
#    0 <= strs[i].length <= 200
#    strs[i] contains any possible characters out of 256 valid ASCII characters.
#
#Follow up: Could you write a generalized algorithm to work on any possible set
#of characters?

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        # Use length prefix encoding: "length#string"
        result = []
        for s in strs:
            result.append(f"{len(s)}#{s}")
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        result = []
        i = 0

        while i < len(s):
            # Find the delimiter
            j = i
            while s[j] != '#':
                j += 1

            # Get length and extract string
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j + 1 + length

        return result


class CodecEscaping:
    """Alternative approach using escape characters"""

    def encode(self, strs: List[str]) -> str:
        """Encode using escape characters"""
        # Escape special characters and use delimiter
        result = []
        for s in strs:
            # Escape backslashes first, then colons
            escaped = s.replace('\\', '\\\\').replace(':', '\\:')
            result.append(escaped)
        return ':'.join(result)

    def decode(self, s: str) -> List[str]:
        """Decode by handling escape characters"""
        result = []
        current = []
        i = 0

        while i < len(s):
            if s[i] == '\\' and i + 1 < len(s):
                current.append(s[i + 1])
                i += 2
            elif s[i] == ':':
                result.append(''.join(current))
                current = []
                i += 1
            else:
                current.append(s[i])
                i += 1

        result.append(''.join(current))
        return result
