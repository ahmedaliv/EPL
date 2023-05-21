class Team:
    def __init__(self,for_goals=0,against_goals=0):
        self.points=0
        self.net_goals=0
        self.for_goals=for_goals
        self.against_goals=against_goals
        self.matches_won=0;
        self.matches_lost=0;
        self.matches_drawn=0;
        self.matches_played=0;
    def calcPoints(self):
        self.points=(self.matches_won*3)+(self.matches_drawn*1)
    def calcNetGoals(self):
        self.net_goals=self.for_goals-self.against_goals

    