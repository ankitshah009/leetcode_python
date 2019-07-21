#871. Minimum Number of Refueling Stops
#Hard
#
#A car travels from a starting position to a destination which is target miles east of the starting position.
#
#Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.
#
#The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.
#
#When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.
#
#What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.
#
#Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.
#
# 
#
#Example 1:
#
#Input: target = 1, startFuel = 1, stations = []
#Output: 0
#Explanation: We can reach the target without refueling.
#
#Example 2:
#
#Input: target = 100, startFuel = 1, stations = [[10,100]]
#Output: -1
#Explanation: We can't reach the target (or even the first gas station).
#
#Example 3:
#
#Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
#Output: 2
#Explanation: 
#We start with 10 liters of fuel.
#We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
#Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
#and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
#We made 2 refueling stops along the way, so we return 2.
#
# 
#
#Note:
#
#    1 <= target, startFuel, stations[i][1] <= 10^9
#    0 <= stations.length <= 500
#    0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target
#

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
	pq = []
        fuel = startFuel
        refuel = 0
        stations = [[0,0]] + stations + [[target,0]]
        for i in range(1, len(stations)): # O(NlgN)
            fuel -= stations[i][0]-stations[i-1][0]
            while fuel < 0:
                if not pq:
                    return -1
                fuel += -heapq.heappop(pq) # O(lgN)
                refuel += 1
            if stations[i][0] >= target:
                return refuel
            heapq.heappush(pq, -stations[i][1])


#### Dynamic programming
#Let's update dp as we consider each station in order. With no stations, clearly we can get a maximum distance of startFuel with 0 refueling stops.

#Now let's look at the update step. When adding a station station[i] = (location, capacity), any time we could reach this station with t refueling stops, we can now reach capacity further with t+1 refueling stops.

#For example, if we could reach a distance of 15 with 1 refueling stop, and now we added a station at location 10 with 30 liters of fuel, then we could potentially reach a distance of 45 with 2 refueling stops.


class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in xrange(i, -1, -1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)

        for i, d in enumerate(dp):
            if d >= target: return i
        return -1


#Approach 2: Heap

#Intuition

#When driving past a gas station, let's remember the amount of fuel it contained. We don't need to decide yet whether to fuel up here or not - for example, there could be a bigger gas station up ahead that we would rather refuel at.

#When we run out of fuel before reaching the next station, we'll retroactively fuel up: greedily choosing the largest gas stations first.
#
#This is guaranteed to succeed because we drive the largest distance possible before each refueling stop, and therefore have the largest choice of gas stations to (retroactively) stop at.
#
#Algorithm
#
#pq ("priority queue") will be a max-heap of the capacity of each gas station we've driven by. We'll also keep track of tank, our current fuel.
#
#When we reach a station but have negative fuel (ie. we needed to have refueled at some point in the past), we will add the capacities of the largest gas stations we've driven by until the fuel is non-negative.
#
#If at any point this process fails (that is, no more gas stations), then the task is impossible.

class Solution(object):
    def minRefuelStops(self, target, tank, stations):
        pq = []  # A maxheap is simulated using negative values
        stations.append((target, float('inf')))

        ans = prev = 0
        for location, capacity in stations:
            tank -= location - prev
            while pq and tank < 0:  # must refuel in past
                tank += -heapq.heappop(pq)
                ans += 1
            if tank < 0: return -1
            heapq.heappush(pq, -capacity)
            prev = location

        return ans
