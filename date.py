from match import Match
from globals import all_dates
class Date:
    def __init__(self,date,match_details):
        self.date=date
        self.matches=[Match(*match_details)]
        all_dates.append(self)
    def add_match(self,match_details):
        self.matches.append(Match(*match_details))
    def __str__(self) -> str:
        return self.date
    def traverse_matches(self):
        for match in self.matches:
            match.play_match()
        
    



