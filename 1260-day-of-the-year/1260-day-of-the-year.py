class Solution:
    def dayOfYear(self, date: str) -> int:
        # Extract year, month, and day
        year, month, day = map(int, date.split('-'))
        
        # Number of days in each month
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Leap year condition
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[1] = 29  # February has 29 days in a leap year
        
        # Sum up the days from previous months and add current day
        return sum(days_in_month[:month - 1]) + day
