from tkinter import ttk
import tkinter as tk
from team import Team
from globals import *

def draw(Teams):
    root = tk.Tk()
    tree = ttk.Treeview(root)
    root.geometry('2000x500')
    tree['columns'] = ('Name', 'MatchPlayed', 'W', 'D', 'L',
                       'Goals For', 'Goals Against', 'Goal Diff', 'Points')
    tree.column('#0', width=7, anchor="w",)
    tree.heading('#0', text='#',anchor="center",)
    tree.heading('Name', text='Name',)
    tree.heading('MatchPlayed', text='MatchPlayed',)
    tree.heading('W', text='W',)
    tree.heading('D', text='D',)
    tree.heading('L', text='L',)
    tree.heading('Goals For', text='Goals For',)
    tree.heading('Goals Against', text='Goals Against',)
    tree.heading('Goal Diff', text='Goal Diff',)
    tree.heading('Points', text='Points',)
    # print(Teams)
    i=1
    for team in Teams: # O(N) where N is the number of teams
        # print(team)
        tree.insert('', 'end', text= i , values=(teams[team].name,
            teams[team].matches_played, teams[team].matches_won, teams[team].matches_drawn, teams[team].matches_lost,
            teams[team].for_goals,
            teams[team].against_goals,
            teams[team].net_goals,
            teams[team].points))
        i+=1
    for column in tree['columns']:
        tree.column(column, anchor='center',width=100)
    
    
    tree.pack(fill='both',expand=True)
    

    root.mainloop()
