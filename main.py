import csv
from round import Round
from globals import *
from team import Team
def add_teams(team1,team2):
    if team1 not in teams:
        teams[team1]=Team()
    if team2 not in teams:
        teams[team2]=Team()
with open('epl_results.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader, None)
    print(headers)
    for row in reader:
        round_number = row[0]
        date   = row[1]
        team1  = row[2]
        team2  = row[3]
        score1 = row[4]
        score2 = row[5]
        winner = row[6]
        add_teams(team1,team2)
        if round_number in rounds:
            # If the round already exists, update its details
            existing_round = rounds[round_number]
            existing_round.add_date_match(date, [team1, team2, score1, score2, winner])
        else:
            # If the round doesn't exist, create a new Round object
            new_round = Round(round_number, date, [team1, team2, score1, score2, winner])
            rounds[round_number] = new_round


# sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
