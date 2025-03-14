class Solution:
    def reformatDate(self, date: str) -> str:
        # Mapping month abbreviations to numbers
        month_map = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }
        
        # Split input into parts
        day, month, year = date.split()
        
        # Extract numerical day and ensure it's two-digit format
        day = ''.join(filter(str.isdigit, day)).zfill(2)
        
        # Format as YYYY-MM-DD
        return f"{year}-{month_map[month]}-{day}"
