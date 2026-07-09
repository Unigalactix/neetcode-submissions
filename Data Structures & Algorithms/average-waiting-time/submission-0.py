class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        kitchen_clock = 0
        total_waiting_time = 0

        for arrival_time, cooking_time in customers:
            kitchen_clock= max(kitchen_clock, arrival_time)
            kitchen_clock += cooking_time
            customer_wait = kitchen_clock - arrival_time
            total_waiting_time += customer_wait
        return total_waiting_time/len(customers)