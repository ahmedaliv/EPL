import csv
from round import Round
from globals import *
from team import Team
from utils import *
from date import Date

def add_teams(team1,team2):
    if team1 not in teams:
        teams[team1]=Team()
    if team2 not in teams:
        teams[team2]=Team()

def read_data():
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
            if round_number in rounds:
                # If the round already exists, update its details
                existing_round = rounds[round_number]
                existing_round.add_date_match(date, [team1, team2, score1, score2, winner])
            else:
                # If the round doesn't exist, create a new Round object
                new_round = Round(round_number, date, [team1, team2, score1, score2, winner])
                rounds[round_number] = new_round

def edit_standing(filter_method,limit):
    if(filter_method=='round'):
        for round_number in rounds:
            if(int(round_number)<=limit):
                for date in rounds[round_number].dates:
                    date.traverse_matches()
    elif(filter_method=='date'):
        for date in all_dates:
            if(date.date<=limit):
                date.traverse_matches()    

def print_standings():
    for team in teams:
        print(f'{team} : {teams[team].matches_won} : {teams[team].matches_drawn} : {teams[team].matches_lost} ');

            
if(__name__ == '__main__'):
    filter_method=int(input("Enter 1 for RoundNumber , 2 for Date: "))
    read_data()
    if(filter_method==1):
        round_number=int(input("Enter the round number: "))
        edit_standing('round',round_number)
    elif(filter_method==2):
        date=convert_date(input("Enter the date: "))
        edit_standing('date',date)
    else:
        print("Invalid Input")
        exit()
    print_standings()
    

