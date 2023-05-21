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

def read_data():
    with open('epl_results.csv', 'r') as csv_file:
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

def edit_standing(filter_method,limit):
    if(filter_method=='round'):
        for round_number in rounds:
            if(int(round_number)<=limit):
                rounds[round_number].traverse_dates()
    elif(filter_method=='date'):
        for date in all_dates:
            if(date.date<=limit):
                date.traverse_matches()    

def export_standings_csv(filename, filter_type=None, filter_value=None):
    if filter_type and filter_value:
        filename = f"standings_{filter_type}_{filter_value}.csv"

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Team', 'MatchPlayed', 'W', 'D', 'L', 'Goals For', 'Goals Against', 'Goal Diff', 'Points'])

        for team in teams:
            writer.writerow([team,
                             teams[team].matches_played,
                             teams[team].matches_won,
                             teams[team].matches_drawn,
                             teams[team].matches_lost,
                             teams[team].for_goals,
                             teams[team].against_goals,
                             teams[team].net_goals,
                             teams[team].points])

def filter_by_round():
    round_number = int(input("Enter the round number: "))
    edit_standing('round', round_number)

def filter_by_date():
    date = convert_date(input("Enter the date: "))
    edit_standing('date', date)

def try_again():
    user_input = input("Would you like to try again? (yes/no): ")
    return user_input.lower() == 'yes'

if __name__ == '__main__':
    while True:
        filter_method = int(input("Please choose an option:\n"
                                  "1. Filter by Round Number\n"
                                  "2. Filter by Date\n"
                                  "Enter the corresponding number: "))
        read_data()

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

        sorted_teams = sorted(teams.items(), key=lambda x: x[1].points, reverse=True)
        teams = dict(sorted_teams)
        export_standings_csv('standings.csv', filter_type, filter_value)
        print(f"Standings exported to standings_{filter_type}_{filter_value}.csv")

        if try_again():
            continue
        else:
            break
