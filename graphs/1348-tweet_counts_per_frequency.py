#1348. Tweet Counts Per Frequency
#Medium
#
#A social media company is trying to monitor activity on their site by analyzing
#the number of tweets that occur in select periods of time. These periods can
#be partitioned into smaller time chunks based on a certain frequency (every
#minute, hour, or day).
#
#For example, the period [10, 10000] (in seconds) would be partitioned into the
#following time chunks with these frequencies:
#    Every minute (60-second chunks): [10,69], [70,129], [130,189], ..., [9970,10000]
#    Every hour (3600-second chunks): [10,3609], [3610,7209], [7210,10000]
#    Every day (86400-second chunks): [10,10000]
#
#Notice that the last chunk may be shorter than the specified frequency's chunk
#size and will always end with the end time of the period (10000 in the above example).
#
#Design the TweetCounts class:
#    TweetCounts() Initializes the TweetCounts object.
#    void recordTweet(String tweetName, int time) Stores the tweetName at the
#    recorded time (in seconds).
#    List<Integer> getTweetCountsPerFrequency(String freq, String tweetName,
#    int startTime, int endTime) Returns a list of integers representing the
#    number of tweets with tweetName in each time chunk for the given period
#    of time [startTime, endTime] (in seconds) and frequency freq.
#
#Constraints:
#    0 <= time, startTime, endTime <= 10^9
#    0 <= endTime - startTime <= 10^4
#    There will be at most 10^4 calls in total to recordTweet and getTweetCountsPerFrequency.

from typing import List
from collections import defaultdict
import bisect

class TweetCounts:
    def __init__(self):
        self.tweets = defaultdict(list)  # tweetName -> sorted list of times
        self.freq_seconds = {
            'minute': 60,
            'hour': 3600,
            'day': 86400
        }

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        chunk_size = self.freq_seconds[freq]
        times = self.tweets[tweetName]

        result = []
        current_start = startTime

        while current_start <= endTime:
            current_end = min(current_start + chunk_size - 1, endTime)

            # Count tweets in [current_start, current_end]
            left = bisect.bisect_left(times, current_start)
            right = bisect.bisect_right(times, current_end)

            result.append(right - left)
            current_start += chunk_size

        return result


class TweetCountsSimple:
    """Simpler implementation without binary search"""

    def __init__(self):
        self.tweets = defaultdict(list)
        self.freq_seconds = {'minute': 60, 'hour': 3600, 'day': 86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        chunk_size = self.freq_seconds[freq]
        num_chunks = (endTime - startTime) // chunk_size + 1

        result = [0] * num_chunks

        for time in self.tweets[tweetName]:
            if startTime <= time <= endTime:
                chunk_idx = (time - startTime) // chunk_size
                result[chunk_idx] += 1

        return result
