import csv
from round import Round
from globals import *
from team import Team
from date import Date
from utils import *

def add_teams(team1,team2):
    if team1 not in teams:
        teams[team1]=Team()
    if team2 not in teams:
        teams[team2]=Team()

def get_standing(filter_type,limit):
    with open('epl_results.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader, None)
        print(headers)
        for row in reader:
            round_number = row[0]
            date   = convert_date(row[1])
            team1  = row[2]
            team2  = row[3]
            score1 = row[4]
            score2 = row[5]
            winner = row[6]
            add_teams(team1,team2)
            if filter_type=='round' :
                if(int(round_number)<=limit):
                        if round_number in rounds:
                            # If the round already exists, update its details
                            existing_round = rounds[round_number]
                            existing_round.add_date_match(date, [team1, team2, score1, score2, winner])
                        else:
                            # If the round doesn't exist, create a new Round object
                            new_round = Round(round_number, date, [team1, team2, score1, score2, winner])
                            rounds[round_number] = new_round
            elif filter_type=='date':
                if(date<=limit):
                    if date in dates:
                        # If the date already exists, update its details
                        existing_date = dates[date]
                        existing_date.add_match([team1, team2, score1, score2, winner])
                    else:
                        # If the date doesn't exist, create a new Date object
                        new_date = Date(date, [team1, team2, score1, score2, winner])
                        dates[date] = new_date
                    
            
            
if(__name__ == '__main__'):
     round_number=int(input("Enter round number: "))
     get_standing('date',convert_date('09/04/2023'))
     for team in teams:
         print(f'{team} : {teams[team].matches_won} : {teams[team].matches_drawn} : {teams[team].matches_lost} ');
    


