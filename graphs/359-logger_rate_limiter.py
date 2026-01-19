#359. Logger Rate Limiter
#Easy
#
#Design a logger system that receives a stream of messages along with their
#timestamps. Each unique message should only be printed at most every 10
#seconds (i.e. a message printed at timestamp t will prevent other identical
#messages from being printed until timestamp t + 10).
#
#All messages will come in chronological order. Several messages may arrive at
#the same timestamp.
#
#Implement the Logger class:
#- Logger() Initializes the logger object.
#- bool shouldPrintMessage(int timestamp, string message) Returns true if the
#  message should be printed in the given timestamp, otherwise returns false.
#
#Example 1:
#Input: ["Logger", "shouldPrintMessage", "shouldPrintMessage",
#        "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage",
#        "shouldPrintMessage"]
#       [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"],
#        [11, "foo"]]
#Output: [null, true, true, false, false, false, true]
#
#Constraints:
#    0 <= timestamp <= 10^9
#    Every timestamp will be passed in non-decreasing order (chronological
#    order).
#    1 <= message.length <= 30
#    At most 10^4 calls will be made to shouldPrintMessage.

class Logger:
    """Simple hash map solution"""

    def __init__(self):
        # Map message to last printed timestamp
        self.message_timestamp = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.message_timestamp:
            self.message_timestamp[message] = timestamp
            return True

        if timestamp - self.message_timestamp[message] >= 10:
            self.message_timestamp[message] = timestamp
            return True

        return False


class LoggerQueue:
    """Using queue with set for O(1) cleanup"""

    def __init__(self):
        from collections import deque
        self.queue = deque()  # (timestamp, message)
        self.message_set = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Clean up old messages
        while self.queue and timestamp - self.queue[0][0] >= 10:
            old_ts, old_msg = self.queue.popleft()
            self.message_set.discard(old_msg)

        if message in self.message_set:
            return False

        self.queue.append((timestamp, message))
        self.message_set.add(message)
        return True


class LoggerBuckets:
    """Using buckets for memory efficiency"""

    def __init__(self):
        # 10 buckets, each bucket stores messages for that second mod 10
        self.buckets = [{} for _ in range(10)]
        self.timestamps = [0] * 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        bucket_idx = timestamp % 10

        # Clear old bucket if timestamp changed
        if self.timestamps[bucket_idx] != timestamp:
            self.buckets[bucket_idx] = {}
            self.timestamps[bucket_idx] = timestamp

        # Check all buckets for the message
        for i in range(10):
            if timestamp - self.timestamps[i] < 10:
                if message in self.buckets[i]:
                    return False

        self.buckets[bucket_idx][message] = timestamp
        return True
