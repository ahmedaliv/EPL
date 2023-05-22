from date import Date
class Round:
    def __init__(self, round_number, date, match_details):
        self.round_number = round_number
        self.dates = [Date(date, match_details)]
        
    def add_date_match(self, date, match_details): # O(D) where D is the number of dates
        for existing_date in self.dates:
            if existing_date.date == date:
                existing_date.add_match(match_details)
                break
        else:
            new_date = Date(date, match_details)
            self.dates.append(new_date)
    def traverse_dates(self): # O(M) where M is the number of matches
        for date in self.dates:
            date.traverse_matches()