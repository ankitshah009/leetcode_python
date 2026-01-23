#1701. Average Waiting Time
#Medium
#
#There is a restaurant with a single chef. You are given an array customers,
#where customers[i] = [arrival_i, time_i]:
#- arrival_i is the arrival time of the ith customer.
#- time_i is the time needed to prepare the order of the ith customer.
#
#When a customer arrives, they give the chef their order, and the chef starts
#preparing it once they are idle. The customer waits till the chef finishes
#preparing their order. The chef does not prepare food for more than one customer
#at a time.
#
#Return the average waiting time of all customers.
#
#Example 1:
#Input: customers = [[1,2],[2,5],[4,3]]
#Output: 5.00000
#
#Example 2:
#Input: customers = [[5,2],[5,4],[10,3],[20,1]]
#Output: 3.25000
#
#Constraints:
#    1 <= customers.length <= 10^5
#    1 <= arrival_i, time_i <= 10^4
#    arrival_i <= arrival_i+1

from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        """
        Simulation - track when chef becomes available.
        """
        total_wait = 0
        chef_free_at = 0

        for arrival, cook_time in customers:
            # Chef starts when they're free or customer arrives (whichever is later)
            start_time = max(chef_free_at, arrival)
            finish_time = start_time + cook_time
            wait_time = finish_time - arrival

            total_wait += wait_time
            chef_free_at = finish_time

        return total_wait / len(customers)


class SolutionVerbose:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        """
        Same approach with more explicit variable names.
        """
        n = len(customers)
        current_time = 0
        total_waiting_time = 0

        for i in range(n):
            arrival_time = customers[i][0]
            preparation_time = customers[i][1]

            # If chef is free before customer arrives, wait for customer
            if current_time < arrival_time:
                current_time = arrival_time

            # Prepare the order
            current_time += preparation_time

            # Customer waits from arrival until order is ready
            waiting_time = current_time - arrival_time
            total_waiting_time += waiting_time

        return total_waiting_time / n
