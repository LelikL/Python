class Date:
    # attribute
    def __init__(self, date_str: str):
        self.date = date_str

    # method
    def __str__(self):
        return f"day: {self.day} month: {self.month} year: {self.year}"

    @classmethod
    def conv(cls, date_str: str):
        date_obj = cls(date_str)
        date_obj.day, date_obj.month, date_obj.year = map(int, date_str.split('-'))
        return date_obj

    @staticmethod
    def valid(date_str: str):
        date_obj = Date.conv(date_str)
        if 0 < date_obj.day <= 31 and 0 < date_obj.month <= 12 and date_obj.year > 0:
            return True
        else:
            return False


print(Date.conv('21-12-2021'))
print(Date.valid('21-12-2021'))
