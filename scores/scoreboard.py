import tkinter as tk
# import symbols as s

score = 0


class Scoreboard():
    def __init__(self, root):
        self.scoreLabel = tk.Label(root, text = 'Your Score ' + str(score), bg = 'powder blue')
        self.scoreLabel.place(x=100, y=100)