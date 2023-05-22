from tkinter import ttk
import tkinter as tk
from team import Team     
def draw(Teams):
    root = tk.Tk()
    tree = ttk.Treeview(root)
    columns=('Team name','MatchPlayed', 'W', 'D', 'L',
            'Goals For', 'Goals Against', 'Goal Diff', 'Points')
    tree = tk.ttk.Treeview(root, columns=columns, show='headings')
    for col in columns:
       tree.heading(col, text=col)
    for team in Teams.keys():
        tree.insert('', 'end', text= team , values=(
            team.matches_played, team.matches_won, team.matches_drawn, team.matches_lost,
            team.for_goals,
            team.against_goals,
            team.net_goals,
            team.points))


# Start the Tkinter event loop
    root.mainloop()
