#1396. Design Underground System
#Medium
#
#An underground railway system is keeping track of customer travel times between
#different stations. They are using this data to calculate the average time it
#takes to travel from one station to another.
#
#Implement the UndergroundSystem class:
#    void checkIn(int id, string stationName, int t)
#        A customer with a card ID equal to id, checks in at the station
#        stationName at time t.
#        A customer can only be checked into one place at a time.
#    void checkOut(int id, string stationName, int t)
#        A customer with a card ID equal to id, checks out from the station
#        stationName at time t.
#    double getAverageTime(string startStation, string endStation)
#        Returns the average time it takes to travel from startStation to
#        endStation.
#        The average time is computed from all the previous traveling times
#        from startStation to endStation that happened directly, meaning a
#        check in at startStation followed by a check out from endStation.
#
#Example 1:
#Input
#["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut",
# "checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
#[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],
# [27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],
# [10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
#Output
#[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]
#
#Constraints:
#    1 <= id, t <= 10^6
#    1 <= stationName.length, startStation.length, endStation.length <= 10
#    All strings consist of uppercase and lowercase English letters and digits.
#    There will be at most 2 * 10^4 calls in total to checkIn, checkOut, and
#    getAverageTime.
#    Answers within 10^-5 of the actual value will be accepted.

from collections import defaultdict

class UndergroundSystem:
    """
    Track check-ins and aggregate travel times between station pairs.
    O(1) for all operations.
    """

    def __init__(self):
        # id -> (station, time) for current check-ins
        self.check_ins = {}
        # (start, end) -> (total_time, count) for completed trips
        self.travel_times = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins.pop(id)
        travel_time = t - start_time

        key = (start_station, stationName)
        self.travel_times[key][0] += travel_time
        self.travel_times[key][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.travel_times[(startStation, endStation)]
        return total_time / count


class UndergroundSystemExplicit:
    """More explicit implementation"""

    def __init__(self):
        self.check_ins = {}  # id -> (station, time)
        self.total_times = defaultdict(int)  # (start, end) -> total time
        self.trip_counts = defaultdict(int)  # (start, end) -> count

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins[id]
        del self.check_ins[id]

        route = (start_station, stationName)
        self.total_times[route] += t - start_time
        self.trip_counts[route] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return self.total_times[route] / self.trip_counts[route]


class UndergroundSystemWithHistory:
    """Version that keeps individual trip history (if needed for analytics)"""

    def __init__(self):
        self.check_ins = {}
        self.trips = defaultdict(list)  # (start, end) -> [times]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins.pop(id)
        self.trips[(start_station, stationName)].append(t - start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.trips[(startStation, endStation)]
        return sum(times) / len(times)
