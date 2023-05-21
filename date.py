from match import Match
class Date:
    def __init__(self,date,match_details):
        self.date=date
        self.matches=[Match(*match_details)]
    def add_match(self,match_details):
        self.matches.append(Match(*match_details))
    
    def __str__(self) -> str:
        return self.date
    

