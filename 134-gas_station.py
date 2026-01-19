#134. Gas Station
#Medium
#
#There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
#
#You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the
#ith station to its next (i + 1)th station. You begin the journey with an empty tank at
#one of the gas stations.
#
#Given two integer arrays gas and cost, return the starting gas station's index if you can
#travel around the circuit once in the clockwise direction, otherwise return -1.
#
#If there exists a solution, it is guaranteed to be unique.
#
#Example 1:
#Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
#Output: 3
#Explanation:
#Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
#Travel to station 4. Your tank = 4 - 1 + 5 = 8
#Travel to station 0. Your tank = 8 - 2 + 1 = 7
#Travel to station 1. Your tank = 7 - 3 + 2 = 6
#Travel to station 2. Your tank = 6 - 4 + 3 = 5
#Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
#
#Example 2:
#Input: gas = [2,3,4], cost = [3,4,3]
#Output: -1
#
#Constraints:
#    n == gas.length == cost.length
#    1 <= n <= 10^5
#    0 <= gas[i], cost[i] <= 10^4

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        current_tank = 0
        starting_station = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            if current_tank < 0:
                starting_station = i + 1
                current_tank = 0

        return starting_station if total_tank >= 0 else -1
