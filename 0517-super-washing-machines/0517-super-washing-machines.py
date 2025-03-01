class Solution:
    def findMinMoves(self, machines):
        total_dresses = sum(machines)
        n = len(machines)

        if total_dresses % n != 0:
            return -1  # Not possible to balance

        target = total_dresses // n
        balance = 0  # Running sum of imbalance
        max_moves = 0
        max_balance = 0  # Max absolute balance at any point

        for dresses in machines:
            balance += dresses - target
            max_moves = max(max_moves, abs(balance))
            max_balance = max(max_balance, dresses - target)

        return max(max_moves, max_balance)
