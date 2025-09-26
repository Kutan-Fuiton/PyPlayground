import numpy as np

class Board:
    def __init__(self):       # Initiate Function
        self.cells = np.array([' ']*9)
    def display(self):        # Display the grid
        print("\n")
        for i in range(3):
            print(" | ".join(self.cells[i*3:(i+1)*3]))
            if i < 2:
                print("--+---+--")
        print("\n")
    def fill_cell(self, pos, symbol):          # Fill the cell with X or 0
        if self.cells[pos] == ' ':
            self.cells[pos] = symbol
            return True
        else:
            print("Cell already occupied. Try again.")
            return False
    def winning_rule(self):         # Rules for winning
        wins = [(0,1,2), (3,4,5), (6,7,8),  # rows
                (0,3,6), (1,4,7), (2,5,8),  # columns
                (0,4,8), (2,4,6)]           # diagonals
        for a,b,c in wins:
            if self.cells[a] == self.cells[b] == self.cells[c] != ' ':
                return self.cells[a]
        return None
    def is_full(self):        # Check for draw
        return 'Draw' if ' ' not in self.cells else None
    

class Game:
    def __init__(self):
        self.board = Board()
        self.current_symbol = 'X'

    def opponent(self, symbol):
        return 'O' if symbol == 'X' else 'X'

    def switch_player(self):
        self.current_symbol = 'O' if self.current_symbol == 'X' else 'X'

    def winning_prediction(self, symbol):
        # symbol = self.opponent(symbol)
        count = 0     # ways to win in 1 step --> count
        for i in range(9):
            if self.board.cells[i] == ' ':
                self.board.cells[i] = symbol
                if self.board.winning_rule() == symbol:
                    count += 1
                self.board.cells[i] = ' '
        return count

    def play(self):
        shorthand = {"lt": 0, "tl": 0, 
                     "top": 1, "t": 1, 
                     "rt": 2, "tr": 2,
                     "left": 3, "l": 3, 
                     "mid": 4, "middle": 4, "m": 4,
                     "right": 5, "r": 5,
                     "lb": 6, "bl": 6, 
                     "bot": 7, "bottom": 7, "b": 7,
                     "rb": 8, "br": 8}
        for j in range(9):
            self.board.display()
            try:
                pos = shorthand[input(f"Player {self.current_symbol}, enter position (1-9): ")] 
                if pos < 0 or pos > 8:
                    print("Invalid position! Choose 1-9.")
                    continue
            except ValueError:
                print("Invalid input! Enter a number 1-9.")
                continue

            if self.board.fill_cell(pos, self.current_symbol):
                # AI Block: Check if opponent can win next move
                if self.winning_prediction(self.current_symbol) >= 2:
                    self.board.display()
                    print(f"Player {self.current_symbol} won! There are no way of blocking...")
                    break
                # Check for win
                if self.board.winning_rule():
                    self.board.display()
                    print(f"Player {self.current_symbol} wins! 🎉")
                    break
                # Check for draw
                if self.board.is_full():
                    self.board.display()
                    print("It's a draw! 🤝")
                    break
                # Switch turn
                self.switch_player()

if __name__ == "__main__":
    game = Game()
    game.play()

