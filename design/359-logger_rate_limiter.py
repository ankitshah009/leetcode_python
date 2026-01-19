#359. Logger Rate Limiter
#Easy
#
#Design a logger system that receives a stream of messages along with their
#timestamps. Each unique message should only be printed at most every 10 seconds
#(i.e. a message printed at timestamp t will prevent other identical messages
#from being printed until timestamp t + 10).
#
#All messages will come in chronological order. Several messages may arrive at
#the same timestamp.
#
#Implement the Logger class:
#    Logger() Initializes the logger object.
#    bool shouldPrintMessage(int timestamp, string message) Returns true if the
#    message should be printed in the given timestamp, otherwise returns false.
#
#Example 1:
#Input
#["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage",
# "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
#[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
#Output
#[null, true, true, false, false, false, true]
#
#Explanation
#Logger logger = new Logger();
#logger.shouldPrintMessage(1, "foo");  // return true
#logger.shouldPrintMessage(2, "bar");  // return true
#logger.shouldPrintMessage(3, "foo");  // return false (within 10 seconds)
#logger.shouldPrintMessage(8, "bar");  // return false (within 10 seconds)
#logger.shouldPrintMessage(10, "foo"); // return false (exactly 10 seconds)
#logger.shouldPrintMessage(11, "foo"); // return true (11 > 1 + 10)
#
#Constraints:
#    0 <= timestamp <= 10^9
#    Every timestamp will be passed in non-decreasing order.
#    1 <= message.length <= 30
#    At most 10^4 calls will be made to shouldPrintMessage.

class Logger:
    def __init__(self):
        self.message_timestamps = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.message_timestamps:
            self.message_timestamps[message] = timestamp
            return True

        if timestamp - self.message_timestamps[message] >= 10:
            self.message_timestamps[message] = timestamp
            return True

        return False


class LoggerWithCleanup:
    """Memory-efficient version that removes old entries"""

    def __init__(self):
        from collections import deque
        self.message_timestamps = {}
        self.queue = deque()  # (timestamp, message)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Clean up old messages
        while self.queue and timestamp - self.queue[0][0] >= 10:
            _, old_msg = self.queue.popleft()
            if self.message_timestamps.get(old_msg) == self.queue[0][0] if self.queue else True:
                del self.message_timestamps[old_msg]

        if message in self.message_timestamps:
            if timestamp - self.message_timestamps[message] >= 10:
                self.message_timestamps[message] = timestamp
                self.queue.append((timestamp, message))
                return True
            return False

        self.message_timestamps[message] = timestamp
        self.queue.append((timestamp, message))
        return True


class LoggerSet:
    """Using set with rolling window"""

    def __init__(self):
        from collections import deque
        self.recent_messages = set()
        self.queue = deque()  # (timestamp, message)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Remove messages older than 10 seconds
        while self.queue and timestamp - self.queue[0][0] >= 10:
            _, old_msg = self.queue.popleft()
            self.recent_messages.discard(old_msg)

        if message in self.recent_messages:
            return False

        self.recent_messages.add(message)
        self.queue.append((timestamp, message))
        return True
