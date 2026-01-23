#1912. Design Movie Rental System
#Hard
#
#You have a movie renting company consisting of n shops. You want to implement
#a renting system that supports searching for, booking, and returning movies.
#The system should also support generating a report of the currently rented
#movies.
#
#Each movie is given as a 2D integer array entries where
#entries[i] = [shop_i, movie_i, price_i] indicates that there is a copy of
#movie movie_i at shop shop_i with a rental price of price_i.
#
#Implement the MovieRentingSystem class:
#- MovieRentingSystem(int n, int[][] entries) Initializes the
#  MovieRentingSystem object with n shops and the movies in entries.
#- List<Integer> search(int movie) Returns the 5 cheapest shops that have an
#  unrented copy of the given movie. If there are less than 5 unrented copies,
#  all of them are returned. Shops are sorted by price in ascending order, and
#  in case of a tie, by shop number.
#- void rent(int shop, int movie) Rents the given movie from the given shop.
#- void drop(int shop, int movie) Drops off a previously rented movie at the
#  given shop.
#- List<List<Integer>> report() Returns the 5 cheapest rented movies (in the
#  form [shop, movie]) as a 2D list. If there are less than 5 rented movies,
#  all of them are returned. Movies are sorted by price in ascending order, and
#  in case of a tie, by shop number, then by movie number.
#
#Constraints:
#    1 <= n <= 3 * 10^5
#    1 <= entries.length <= 10^5
#    0 <= shop_i < n
#    1 <= movie_i, price_i <= 10^4
#    Each shop carries at most one copy of a movie movie_i.
#    At most 10^5 calls in total will be made to search, rent, drop and report.

from typing import List
from collections import defaultdict
from sortedcontainers import SortedList

class MovieRentingSystem:
    """
    Using SortedList for efficient operations.
    """

    def __init__(self, n: int, entries: List[List[int]]):
        # movie -> SortedList of (price, shop) for unrented copies
        self.unrented = defaultdict(SortedList)
        # SortedList of (price, shop, movie) for rented copies
        self.rented = SortedList()
        # (shop, movie) -> price
        self.prices = {}

        for shop, movie, price in entries:
            self.unrented[movie].add((price, shop))
            self.prices[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        # Return top 5 cheapest shops for this movie
        return [shop for price, shop in self.unrented[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.unrented[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.unrented[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for price, shop, movie in self.rented[:5]]


class MovieRentingSystemHeap:
    """
    Using heaps with lazy deletion.
    """

    def __init__(self, n: int, entries: List[List[int]]):
        import heapq

        self.unrented = defaultdict(list)  # movie -> heap of (price, shop)
        self.rented_set = set()  # (shop, movie) currently rented
        self.prices = {}

        for shop, movie, price in entries:
            heapq.heappush(self.unrented[movie], (price, shop))
            self.prices[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        import heapq

        result = []
        temp = []

        while self.unrented[movie] and len(result) < 5:
            price, shop = heapq.heappop(self.unrented[movie])
            if (shop, movie) not in self.rented_set:
                result.append(shop)
            temp.append((price, shop))

        # Restore heap
        for item in temp:
            heapq.heappush(self.unrented[movie], item)

        return result

    def rent(self, shop: int, movie: int) -> None:
        self.rented_set.add((shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rented_set.discard((shop, movie))

    def report(self) -> List[List[int]]:
        # Get all rented with prices
        rented_list = [(self.prices[(s, m)], s, m) for s, m in self.rented_set]
        rented_list.sort()
        return [[s, m] for p, s, m in rented_list[:5]]
