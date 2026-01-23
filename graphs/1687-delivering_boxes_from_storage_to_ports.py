#1687. Delivering Boxes from Storage to Ports
#Hard
#
#You have the task of delivering some boxes from storage to their ports using
#only one ship. However, this ship has a limit on the number of boxes and the
#total weight that it can carry.
#
#You are given an array boxes, where boxes[i] = [ports_i, weight_i], and three
#integers portsCount, maxBoxes, and maxWeight.
#- ports_i is the port where you need to deliver the ith box.
#- weight_i is the weight of the ith box.
#- portsCount is the number of ports.
#- maxBoxes is the maximum number of boxes the ship can carry.
#- maxWeight is the maximum weight the ship can carry.
#
#The boxes need to be delivered in the order they are given. The ship can follow
#these steps:
#- The ship will take some boxes and sail to a port.
#- At the port, it unloads all boxes destined for that port.
#- It then sails to the next port and repeats until all boxes are delivered.
#
#Note that the ship must end at the storage after delivering all boxes.
#
#Return the minimum number of trips the ship needs to make to deliver all boxes.
#
#Example 1:
#Input: boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3
#Output: 4
#Explanation: The optimal strategy is:
#- Ship takes boxes 0, 1, 2. Trips: storage->1->2->1->storage. 4 trips.
#
#Example 2:
#Input: boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6
#Output: 6
#
#Constraints:
#    1 <= boxes.length <= 10^5
#    1 <= portsCount, maxBoxes, maxWeight <= 10^5
#    1 <= ports_i <= portsCount
#    1 <= weights_i <= maxWeight

from typing import List
from collections import deque

class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int,
                      maxBoxes: int, maxWeight: int) -> int:
        """
        DP with sliding window optimization.
        dp[i] = min trips to deliver first i boxes
        """
        n = len(boxes)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # Precompute cost changes (port transitions)
        diff = [0] * n
        for i in range(1, n):
            diff[i] = 1 if boxes[i][0] != boxes[i-1][0] else 0

        # Sliding window
        j = 0  # Start of window
        weight = 0
        cost = 0  # Number of port changes in current window

        dq = deque([0])  # Monotonic deque for minimum dp value

        for i in range(n):
            # Add box i to window
            weight += boxes[i][1]
            if i > 0:
                cost += diff[i]

            # Shrink window from left if constraints violated
            while j <= i and (i - j + 1 > maxBoxes or weight > maxWeight):
                weight -= boxes[j][1]
                if j < i:
                    cost -= diff[j + 1]
                j += 1

                # Remove elements from deque that are out of window
                while dq and dq[0] < j:
                    dq.popleft()

            # dp[i+1] = min(dp[k] + cost[k+1:i+1] + 2) for j <= k <= i
            # We need: dp[k] - prefix_cost[k+1] + cost[0:i+1] + 2
            # Rearranging: (dp[k] - prefix_cost[k+1]) is what we minimize

            # But simpler: with prefix cost handling
            # dp[i+1] = dp[j] + cost (from j to i) + 2
            # where cost is number of different consecutive ports

            if dq:
                dp[i + 1] = dp[dq[0]] + cost + 2

            # Maintain monotonic deque for next iteration
            # We want to minimize dp[k] - (cost from k+1 to current)
            while dq and dp[dq[-1]] - sum(diff[dq[-1]+1:i+2] if dq[-1]+1 <= i else 0) >= \
                         dp[i+1] - 0:
                dq.pop()
            dq.append(i + 1)

        return dp[n]


class SolutionOptimized:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int,
                      maxBoxes: int, maxWeight: int) -> int:
        """
        Optimized DP with monotonic deque.
        """
        n = len(boxes)

        # dp[i] = min trips to deliver boxes[0:i]
        dp = [0] + [float('inf')] * n

        # Number of port transitions up to each box
        transitions = [0] * (n + 1)
        for i in range(1, n):
            transitions[i + 1] = transitions[i] + (1 if boxes[i][0] != boxes[i-1][0] else 0)

        j = 0  # Left pointer
        weight = 0
        dq = deque()  # Stores (index, dp[index] - transitions[index+1])

        for i in range(n):
            weight += boxes[i][1]

            # Shrink window
            while i - j + 1 > maxBoxes or weight > maxWeight:
                weight -= boxes[j][1]
                j += 1

            # Remove out-of-window elements
            while dq and dq[0][0] < j:
                dq.popleft()

            # Add j-1 to deque if valid
            if j > 0:
                val = dp[j-1] - transitions[j]
                while dq and dq[-1][1] >= val:
                    dq.pop()
                dq.append((j-1, val))

            # Also consider starting fresh from j
            if not dq or dp[j] - transitions[j+1] < dq[0][1]:
                val = dp[j] - transitions[j+1]
                while dq and dq[-1][1] >= val:
                    dq.pop()
                dq.append((j, val))

            # Compute dp[i+1]
            if dq:
                dp[i+1] = dq[0][1] + transitions[i+1] + 2

        return dp[n]


class SolutionSimple:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int,
                      maxBoxes: int, maxWeight: int) -> int:
        """
        Simpler DP approach (may be slower but clearer).
        """
        n = len(boxes)
        dp = [0] + [float('inf')] * n

        for i in range(n):
            # Try all valid starting points j
            j = i
            weight = 0
            ports = 0
            prev_port = -1

            while j >= 0 and i - j + 1 <= maxBoxes:
                weight += boxes[j][1]
                if weight > maxWeight:
                    break

                if boxes[j][0] != prev_port:
                    ports += 1
                    prev_port = boxes[j][0]

                dp[i + 1] = min(dp[i + 1], dp[j] + ports + 1)
                j -= 1

        return dp[n]
