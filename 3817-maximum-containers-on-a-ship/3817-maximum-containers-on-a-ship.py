class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        total_slots = n * n
        max_weight_containers = maxWeight // w
        return min(total_slots, max_weight_containers)
