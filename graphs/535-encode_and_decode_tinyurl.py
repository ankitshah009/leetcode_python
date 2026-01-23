#535. Encode and Decode TinyURL
#Medium
#
#TinyURL is a URL shortening service where you enter a URL such as
#https://leetcode.com/problems/design-tinyurl and it returns a short URL such as
#http://tinyurl.com/4e9iAk.
#
#Design a class to encode a URL and decode a tiny URL.
#
#There is no restriction on how your encode/decode algorithm should work. You just
#need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be
#decoded to the original URL.
#
#Implement the Solution class:
#- Solution() Initializes the object of the system.
#- String encode(String longUrl) Returns a tiny URL for the given longUrl.
#- String decode(String shortUrl) Returns the original long URL for the given shortUrl.
#
#Constraints:
#    1 <= url.length <= 10^4
#    url is guaranteed to be a valid URL.

import random
import string

class Codec:
    """Using random code generation"""

    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.chars = string.ascii_letters + string.digits
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.url_to_code:
            return self.base + self.url_to_code[longUrl]

        # Generate random 6-character code
        while True:
            code = ''.join(random.choice(self.chars) for _ in range(6))
            if code not in self.code_to_url:
                break

        self.url_to_code[longUrl] = code
        self.code_to_url[code] = longUrl

        return self.base + code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        code = shortUrl.replace(self.base, "")
        return self.code_to_url.get(code, "")


class CodecCounter:
    """Using incrementing counter"""

    def __init__(self):
        self.counter = 0
        self.url_map = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        self.counter += 1
        self.url_map[self.counter] = longUrl
        return self.base + str(self.counter)

    def decode(self, shortUrl: str) -> str:
        code = int(shortUrl.replace(self.base, ""))
        return self.url_map.get(code, "")


class CodecHash:
    """Using hash of URL"""

    def __init__(self):
        self.url_map = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        code = hash(longUrl)
        self.url_map[code] = longUrl
        return self.base + str(code)

    def decode(self, shortUrl: str) -> str:
        code = int(shortUrl.replace(self.base, ""))
        return self.url_map.get(code, "")
