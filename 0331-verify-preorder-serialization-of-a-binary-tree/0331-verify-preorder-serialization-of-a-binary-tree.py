class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(",")
        slots = 1  # Start with one slot for the root
        
        for node in nodes:
            slots -= 1  # Every node consumes a slot
            
            if slots < 0:
                return False  # If slots become negative, it's invalid
            
            if node != "#":
                slots += 2  # Non-null nodes add two slots
        
        return slots == 0  # Must end with exactly 0 slots