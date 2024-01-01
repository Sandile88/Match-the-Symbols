import tkinter as tk
import random as r
import scores.scoreboard as s


class SymbolGame():
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x250')
        self.root.title('Guess The Symbols')
        self.symbols = [
            "★", "☆", "✦", "✧", "✪", "✫", "✯", "✰", "✵", "✶",  # Stars
            "♈", "♉", "♊", "♋", "♌", "♍", "♎", "♏", "♐", "♑", "♒", "♓",  # Zodiac Signs
            "🐾", "🐯", "🐘", "🦁", "🦄", "🦓", "🦒", "🐆", "🐅", "🐊", "🐃",  # Animals
            "🌹", "🌻", "🌼", "🌷", "🌸", "🌺", "🌵", "🍁", "🍀", "🍂",  # Flowers and Plants
            "☯", "☮", "☪", "☸", "♈", "♉", "♊", "♋", "♌", "♍", "♎", "♏", "♐", "♑", "♒", "♓",  # Miscellaneous Symbols
            "⚛", "⚜", "⚓", "⚔", "⚖", "⚗", "⚙", "⚛", "⚜", "⚠", "⚡", "⚢", "⚣", "⚤", "⚥",  # More Miscellaneous Symbols
        ]
        self.computer_lineup = []
        self.user_lineup = []
        self.scoreboard = s.Scoreboard(root)
        # self.num_symbols = 0

        self.generate_computer_lineup()
        self.create_gui()


    def generate_computer_lineup(self):
        level = self.choose_level()
        self.computer_lineup = r.sample(self.symbols, level)
        
    def create_gui(self):
        tk.Label(self.root, text='Match the lineup!').pack

        computer_lineup = tk.Label(
            self.root,
            text = f'Get ready. Game starts in {self.scoreboard.get_countdown()}. GO!'
            f'{" ".join(self.computer_lineup)}',
            foreground='white',
            background='blue'
        )
        computer_lineup.pack()

        # self.get_user_input()

        user_input = tk.Entry(self.root, text = 'What is the order of the symbols?: ', fg='black', bg='yellow')
        user_input.pack()

        submit = tk.Button(self.root, text='Submit', command=lambda: self.is_winner(user_input.get()))
        submit.pack()
    
        
    def get_user_name(self):
        name = tk.Entry(self.root, text='Please enter your name:')
        while len(name.get()) == 0:
            name = tk.Entry(self.root, text='Please enter your name:')
        return name.get()


    def is_winner(self, user_input):
        self.user_lineup = user_input.split()

        if self.user_lineup == self.computer_lineup:
            text = tk.Label(self.root, text='Good job! You win.')
            s.score += 2
            s.Scoreboard.set_text(text = 'Your score ' + str(s.score))
            
        else:
            text = tk.Label('You lost.')
            text = tk.Label(f'The correct order was : {self.computer_lineup}')

        result_label= tk.Label(self.root, text=text)
        result_label.pack()


    def countdown(self, count):
        if count > 0:
            root.after(1000, self.countdown(3), root, count-1)


    def replay(self):
        replay_button = tk.Button(self.root, text = 'Play', cmd=self.run_game)
        return replay_button


    def menu(self):
        tk.Label('What would you like to do?: ')
        self.choose_level()
        self.display_info()


    def choose_level(self):
        tk.Label(self.root, text= 'Start: ').pack()
        easy_button =  tk.Button(self.root, text='Easy', cmd= lambda: self.start_game(1, 10))
        easy_button.pack()
        medium_button =  tk.Button(self.root, text='Medium', cmd= lambda: self.start_game(7, 20))
        medium_button.pack()
        hard_button =  tk.Button(self.root, text='Hard', cmd= lambda: self.start_game(10, 30))
        hard_button.pack()
        
        
    def start_game(self, min_symbols, max_symbols):
        level = r.randint(min_symbols, max_symbols)
        self.computer_lineup = r.sample(self.symbols, level)
        self.create_gui()


    def display_info(self):
        tk.Button(self.root, text='Instructions')
        tk.Label(self.root, text='''How to play the game?
    - Win the game by replicating the symbols showed by the GameMaster.
    - Be careful! The more you win, the faster the GameMaster shows the symbols!
    - Do your best to keep up!''')


    def run_game(self):
        print('Welcome to Replicate The Symbols!')

        while True:
            name = self.get_user_name()
            tk.Label(self.root, text= f'Hello {name}! Welcome to Guess the Symbols Game!')
            if not self.is_winner(name):
                tk.Button(self.root, text='Play again', command=self.run_game()).pack()
                self.replay(self)
            else:
                continue


if __name__ == '__main__':
    root = tk.Tk()
    game = SymbolGame(root)
    root.mainloop()



        
    