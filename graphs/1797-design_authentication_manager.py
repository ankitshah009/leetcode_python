#1797. Design Authentication Manager
#Medium
#
#There is an authentication system that works with authentication tokens. For
#each session, the user will receive a new authentication token that will expire
#timeToLive seconds after the currentTime. If the token is renewed, the expiry
#time will be extended to expire timeToLive seconds after the (potentially
#different) currentTime.
#
#Implement the AuthenticationManager class:
#- AuthenticationManager(int timeToLive) constructs the AuthenticationManager
#  and sets the timeToLive.
#- generate(string tokenId, int currentTime) generates a new token with the
#  given tokenId at the given currentTime in seconds.
#- renew(string tokenId, int currentTime) renews the unexpired token with the
#  given tokenId at the given currentTime in seconds. If there are no unexpired
#  tokens with the given tokenId, the request is ignored.
#- countUnexpiredTokens(int currentTime) returns the number of unexpired tokens
#  at the given currentTime.
#
#Note that if a token expires at time t, and another action happens on time t
#(renew or countUnexpiredTokens), the expiration takes place before the other
#actions.
#
#Example 1:
#Input:
#["AuthenticationManager", "renew", "generate", "countUnexpiredTokens", "generate", "renew", "renew", "countUnexpiredTokens"]
#[[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]
#Output: [null, null, null, 1, null, null, null, 0]
#
#Constraints:
#    1 <= timeToLive <= 10^8
#    1 <= currentTime <= 10^8
#    1 <= tokenId.length <= 5
#    tokenId consists only of lowercase letters.
#    All calls to generate will contain unique values of tokenId.
#    The values of currentTime across all calls are strictly increasing.
#    At most 2000 calls will be made to all functions combined.

class AuthenticationManager:
    """
    Simple dict-based implementation.
    """

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = {}  # tokenId -> expiry time

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(1 for expiry in self.tokens.values() if expiry > currentTime)


class AuthenticationManagerOptimized:
    """
    With periodic cleanup to save memory.
    """

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = {}
        self.cleanup_threshold = 1000

    def _cleanup(self, currentTime: int):
        """Remove expired tokens."""
        expired = [tid for tid, exp in self.tokens.items() if exp <= currentTime]
        for tid in expired:
            del self.tokens[tid]

    def generate(self, tokenId: str, currentTime: int) -> None:
        if len(self.tokens) > self.cleanup_threshold:
            self._cleanup(currentTime)
        self.tokens[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self._cleanup(currentTime)
        return len(self.tokens)


class AuthenticationManagerDeque:
    """
    Using OrderedDict for efficient expiration tracking.
    """
    from collections import OrderedDict

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = self.OrderedDict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.ttl
        self.tokens.move_to_end(tokenId)

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.ttl
            self.tokens.move_to_end(tokenId)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        # Remove expired from front
        while self.tokens:
            oldest_id = next(iter(self.tokens))
            if self.tokens[oldest_id] <= currentTime:
                del self.tokens[oldest_id]
            else:
                break
        return len(self.tokens)
