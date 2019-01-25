#tictactoe_lab_26
class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __eq__(self, other):
        if type(other) is Player:
            return self.token == other.token

    def __repr__(self):
        return self.token


class Game:
    def __init__(self):
        # self.positions = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
        self.board = [[" " for i in range(3)] for j in range(3)] #[["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]


    def __repr__(self):
        # Returns a pretty string representation of the game board
        rows = []
        for i in range(len(self.board)):
            rows.append("|".join(self.board[i]))
        return "\n".join(rows)


    def move(self, x, y, token):
        # Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
        if self.board[x][y] == "X" or self.board[x][y] == "O":
            return "That move has already been played. Please try again."
        else:
            self.board[x][y] = token
        # print(f"Player {player.name} placed a {player.token} on position number {positions}")
        # print(self.board)


    def calc_winner(self):
        # What token character string has won or None if no one has.
        # a for loop that checks i, the chosen input move of the player, in the range and length of self.board
        for i in range(3): #(len(self.board)):
            # checks for a win in row
            row = self.board[i]
            if all(item == row[0] and item != " " for item in row):
                return row[0]
            # checks for a win in column
            column = [self.board[j][i] for j in range(3)] #(len(self.board))]
            if all(item == column[0] and item != " " for item in column):
                return column[0]
        # lines 44 - 49 checks for wins in the 2 diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and self.board[0][0] != " ":
            return self.board[0][0]

        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[2][0] != " ":
            return self.board[0][2]


    def is_full(self):
        # Returns true if the game board is full.
        for row in self.board:
            if any(item == " " for item in row):
                return False
        return True


    def is_game_over(self):
        # Returns true if the game board is full or a player has won.
        return self.calc_winner() or self.is_full()


def main():
# REPL goes under this function
    positions = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}
    while True:
        game = Game()
        player_1 = Player(input("What's your name? > "), "X")
        print(player_1.name, player_1.token)
        player_2 = Player(input("What's your name? > "), "O")
        print(player_2.name, player_2.token)
        print(game)
        game_round = 1
        # print(f"Round {game_round}.")

        while not game.is_game_over():
            current_player = player_1 if game_round % 2 else player_2

            while True:
                move = input(f"{current_player.name} What is your move? > ").strip()
                try:
                    move = int(move)
                    if 1 <= move <= 9:
                        x, y = positions[move]
                        move = game.move(x, y, current_player.token)
                        if type(move) is str:
                            raise IndexError("You can't make that move.")
                        print(game)
                        game_round += 1
                        break
                    else:
                        raise IndexError("You can't make that move.")
                except (ValueError, IndexError):
                    print("You can't make that move, please choose an open space between 1 - 9.")
                    # player_1_move = int(input(f"What is your move {player_1.name}? > "))
                    # print(player_1_move)
                    # game.move(player_1_move, player_1)
                    # player_2_move = int(input(f"What is your move {player_2.name}? > "))
                    # game.move(player_2_move, player_2)
                    # if move in player_1_move:
        if not game.is_full():
            print(f"And that's game! The winner is {game.calc_winner()}")
        else:
            print("The game ends in a tie! You're evenly matched.")

        exit = input("Would you like to play again? > ")
        if exit != "yes":
            break

main()
