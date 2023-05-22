import csv
from round import Round
from globals import *
from team import Team
from date import Date
from utils import *
from support import *
def add_teams(team1,team2):
    if team1 not in teams:
        teams[team1]=Team(team1)
    if team2 not in teams:
        teams[team2]=Team(team2)

def read_data(): # O(M) where M is the number of matches
    with open('EPL-main\epl_results.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader, None)
        for row in reader:
            round_number = int(row[0])
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

def edit_standing(filter_method,limit): # O(M) where M is the number of matches
    if(filter_method=='round'):
        for round_number in rounds:
            if(int(round_number)<=limit):   
                rounds[round_number].traverse_dates()
                
    elif(filter_method=='date'):
        for date in all_dates:
            if(date.date<=limit):
                date.traverse_matches()    

def filter_by_round(): # O(M) where M is the number of matches
    round_number = int(input("Enter the round number: "))
    edit_standing('round', round_number)

def filter_by_date(): # O(M) where M is the number of matches
    date = convert_date(input("Enter the date: "))
    edit_standing('date', date)

def try_again(): # O(1)
    user_input = input("Would you like to try again? (yes/no): ")
    return user_input.lower() == 'yes'

def clear_all_teams(): # O(N) where N is the number of teams
    for team in teams.values():
        team.clear_data()
        
                
if __name__ == '__main__': # O(NlogN) where N is the number of teams
    read_data()
    while True:
        filter_method = int(input("Please choose an option:\n"
                                  "1. Filter by Round Number\n"
                                  "2. Filter by Date\n"
                                  "Enter the corresponding number: "))
        if filter_method == 1:
            round_number = int(input("Enter the round number: "))
            edit_standing('round', round_number)
            filter_type = 'round'
            filter_value = round_number
        elif filter_method == 2:
            date = convert_date(input("Enter the date: "))
            edit_standing('date', date)
            filter_type = 'date'
            filter_value = date
        else:
            print("Invalid Input")
            if not try_again():
                exit()
        sorted_teams = sorted(teams.items(), key=lambda x: x[1].score, reverse=True)
        teams = dict(sorted_teams)
        draw(teams)
        clear_all_teams()
        print("----------")
        if try_again():
            continue
        else:
            break

