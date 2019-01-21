#tictactoe_lab_26
class Player:
    def __init__(self):
        self.name = input("What is your name? > ")
        self.token = "X" or "O"


class Game:
    def __init__(self):
        self.game_board = ["|1", "|2|", "3|", "|4", "|5|", "6|", "|7", "|8|", "9|"]
        self.positons = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
    
    def __repr__(self):
        pass


    def move(self, player, location):
        self.game_board[location -1] = player
        print(self.game_board)

def main():
    pass