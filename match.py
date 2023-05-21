from globals import teams
class Match:
    def __init__(self, team1, team2, score1, score2, winner):
        self.team1=team1
        self.team2=team2
        self.score1=int(score1)
        self.score2=int(score2)
        self.winner=winner
        self.edit_standing()

    def edit_standing(self):
        if(self.winner=='H'):
            teams[self.team1].matches_won+=1
            teams[self.team2].matches_lost+=1
        elif(self.winner=='A'):
            teams[self.team2].matches_won+=1
            teams[self.team1].matches_lost+=1
        else:
            teams[self.team1].matches_drawn+=1
            teams[self.team2].matches_drawn+=1
        teams[self.team1].for_goals+=self.score1
        teams[self.team1].against_goals+=self.score2
        teams[self.team2].for_goals+=self.score2
        teams[self.team2].against_goals+=self.score1
    def __str__(self) -> str:
        return f"{self.team1} vs {self.team2} ({self.score1}-{self.score2})"
    