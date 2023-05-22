class Team:
    def __init__(self,name,for_goals=0,against_goals=0):
        self.name=name
        self.points=0
        self.net_goals=0
        self.for_goals=for_goals
        self.against_goals=against_goals
        self.matches_won=0
        self.matches_lost=0
        self.matches_drawn=0
        self.matches_played=0
        self.score=0
    def calcPoints(self): # O(1)
        self.points=(self.matches_won*3)+(self.matches_drawn*1)
    def calcNetGoals(self): # O(1)
        self.net_goals=self.for_goals-self.against_goals
    def calScore(self): # O(1)
        self.score = 1000*self.points + self.net_goals
    def clear_data(self): # O(1)
        for attr in self.__dict__:
            if attr != "name":
                setattr(self, attr, 0)
