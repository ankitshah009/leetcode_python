#1410. HTML Entity Parser
#Medium
#
#HTML entity parser is the parser that takes HTML code as input and replace all
#the entities of the special characters by the characters itself.
#
#The special characters and their entities for HTML are:
#    Quotation Mark: the entity is &quot; and symbol character is ".
#    Single Quote Mark: the entity is &apos; and symbol character is '.
#    Ampersand: the entity is &amp; and symbol character is &.
#    Greater Than Sign: the entity is &gt; and symbol character is >.
#    Less Than Sign: the entity is &lt; and symbol character is <.
#    Slash: the entity is &frasl; and symbol character is /.
#
#Given the input text string to the HTML parser, you have to implement the
#entity parser.
#
#Return the text after replacing the entities by the special characters.
#
#Example 1:
#Input: text = "&amp; is an HTML entity but &ambassador; is not."
#Output: "& is an HTML entity but &ambassador; is not."
#
#Example 2:
#Input: text = "and I quote: &quot;...&quot;"
#Output: "and I quote: \"...\""
#
#Constraints:
#    1 <= text.length <= 10^5
#    The string may contain any possible characters out of all the 256 ASCII characters.

class Solution:
    def entityParser(self, text: str) -> str:
        """
        Replace HTML entities with their corresponding characters.
        Order matters: replace &amp; last to avoid double replacement.
        """
        # Map of entities to characters
        entities = {
            '&quot;': '"',
            '&apos;': "'",
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/',
            '&amp;': '&'  # Must be last to avoid replacing & in other entities
        }

        for entity, char in entities.items():
            text = text.replace(entity, char)

        return text


class SolutionSinglePass:
    def entityParser(self, text: str) -> str:
        """Single pass approach"""
        entities = {
            '&quot;': '"',
            '&apos;': "'",
            '&amp;': '&',
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/'
        }

        result = []
        i = 0
        n = len(text)

        while i < n:
            if text[i] == '&':
                # Try to match an entity
                found = False
                for entity, char in entities.items():
                    if text[i:i+len(entity)] == entity:
                        result.append(char)
                        i += len(entity)
                        found = True
                        break

                if not found:
                    result.append(text[i])
                    i += 1
            else:
                result.append(text[i])
                i += 1

        return ''.join(result)


class SolutionRegex:
    def entityParser(self, text: str) -> str:
        """Using regex for replacement"""
        import re

        entities = {
            '&quot;': '"',
            '&apos;': "'",
            '&amp;': '&',
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/'
        }

        def replace(match):
            entity = match.group(0)
            return entities.get(entity, entity)

        # Pattern matches any of the entities
        pattern = '|'.join(re.escape(e) for e in entities.keys())
        return re.sub(pattern, replace, text)
