from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort boxes by the number of units per box in descending order
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        max_units = 0  # To store the total units
        for num_boxes, units_per_box in boxTypes:
            if truckSize == 0:
                break  # Stop if the truck is full
            # Take as many boxes as possible
            boxes_to_take = min(truckSize, num_boxes)
            max_units += boxes_to_take * units_per_box
            truckSize -= boxes_to_take  # Reduce available space

        return max_units
