class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [big, medium, small]  # Store available spaces for each car type

    def addCar(self, carType: int) -> bool:
        if self.spaces[carType - 1] > 0:  # Check if space is available
            self.spaces[carType - 1] -= 1  # Reduce available slot
            return True
        return False
