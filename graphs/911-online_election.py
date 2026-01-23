#911. Online Election
#Medium
#
#You are given two integer arrays persons and times. In an election, the i-th
#vote was cast for persons[i] at time times[i].
#
#For each query at time t, find the person that was leading the election at
#time t. Votes cast at time t will count towards our query.
#
#Implement the TopVotedCandidate class:
#- TopVotedCandidate(int[] persons, int[] times) Initializes the object.
#- int q(int t) Returns the number of the person that was leading at time t.
#
#Example 1:
#Input: ["TopVotedCandidate","q","q","q","q","q","q"]
#       [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
#Output: [null,0,1,1,0,0,1]
#
#Constraints:
#    1 <= persons.length <= 5000
#    times.length == persons.length
#    0 <= persons[i] < persons.length
#    0 <= times[i] <= 10^9
#    times is sorted in strictly increasing order.
#    At most 10^4 calls will be made to q.

import bisect

class TopVotedCandidate:
    """
    Precompute leader at each time, use binary search for queries.
    """

    def __init__(self, persons: list[int], times: list[int]):
        self.times = times
        self.leaders = []

        votes = {}
        leader = -1
        max_votes = 0

        for person in persons:
            votes[person] = votes.get(person, 0) + 1

            # >= because ties go to most recent vote
            if votes[person] >= max_votes:
                max_votes = votes[person]
                leader = person

            self.leaders.append(leader)

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times, t) - 1
        return self.leaders[idx]


class TopVotedCandidateAlt:
    """Alternative with explicit counts"""

    def __init__(self, persons: list[int], times: list[int]):
        self.times = times
        self.leaders = []

        from collections import defaultdict
        votes = defaultdict(int)
        leader = persons[0]

        for person in persons:
            votes[person] += 1
            if votes[person] >= votes[leader]:
                leader = person
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        # Find rightmost time <= t
        lo, hi = 0, len(self.times) - 1

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.times[mid] <= t:
                lo = mid
            else:
                hi = mid - 1

        return self.leaders[lo]
