#connect4_lab_27.py
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
    width_column = 7
    height_row = 6


    def __init__(self):
        self.board = [["4" for column in range(self.width_column)] for row in range(self.height_row)]


    def __repr__(self):
        rows = []
        for i in range(len(self.board)):
            rows.append("|".join(self.board[i]))
        return "\n".join(rows)


    def get_height(self, position):
        for i in range(self.height_row - 1, - 1, - 1):
            if self.board[i][position] == "4":
                return i
        return False


    def move(self, player_token, position):
        board_height = self.get_height(position)
        if type(board_height) is bool:
            print("This column is full, please select another.")
            return False
        self.board[board_height][position] = player_token


    def calc_winner(self):
        for i in range(self.height_row - 1, - 1, - 1):
            for j in range(self.width_column):

                # this section checks for horizontal wins
                if j < self.width_column - 3:
                    board_section = self.board[i][j: j + 4]
                    if all(item == self.board[i][j] and item != "4" for item in board_section):
                        return self.board[i][j]

                # this section checks for vertical wins
                if i < self.height_row - 3:
                    board_section = []
                    board_section.append(self.board[i][j])
                    board_section.append(self.board[i + 1][j])
                    board_section.append(self.board[i + 2][j])
                    board_section.append(self.board[i + 3][j])
                    if all(item == self.board[i][j] and item != "4" for item in board_section):
                        return self.board[i][j]

                # this section checks for diagonal wins
                if i < self.height_row - 3 and j < self.width_column - 3:
                    board_section = []
                    board_section.append(self.board[i][j : j + 4])
                    board_section.append(self.board[i + 1][j: j + 4])
                    board_section.append(self.board[i + 2][j: j + 4])
                    board_section.append(self.board[i + 3][j: j + 4])

                    if board_section[0][0] == board_section[1][1] == board_section[2][2] == board_section[3][3] and board_section[0][0] != "4":
                        return board_section[0][0]
                    elif board_section[3][0] == board_section[1][2] == board_section[2][1] == board_section[0][3] and board_section[3][0] != "4":
                        return board_section[3][0]


    def is_full(self):
        for row in self.board:
            if any(space == "4" for space in row):
                return False
        return True


    def is_game_over(self):
        return self.calc_winner() or self.is_full()


def main():
    # board_positions = range(7)
    while True:
        game = Game()
        print("Let's play a game of Connect Four.")
        player_1 = Player(input("Player 1, what's your name? > "), "X")
        print(player_1.name, player_1.token)
        player_2 = Player(input("Player 2, what's your name? > "), "O")
        print(player_2.name, player_2.token)
        print(game)
        game_round = 1

        while not game.is_game_over():
            current_player = player_1 if game_round % 2 else player_2

            while True:
                move = input(f"{current_player.name} What is your move? > ").strip()
                try:
                    move_token = int(move)
                    # print(current_player.token)
                    if 1 <= move_token <= 7:
                        # column = board_positions[move]
                        game.move(current_player.token, move_token - 1)
                        if type(move_token) is str:
                            raise IndexError("You can't make that move.")
                        print(game)
                        game_round += 1
                        break
                    else:
                        raise IndexError("You can't make that move.")
                except (ValueError, IndexError):
                    print("You can't make that move, please choose an open column between 1 - 7.")

        if not game.is_full():
            # continue
            print(f"And that's game! The winner is {game.calc_winner()}")
        else:
            print("The game ends in a tie! You're evenly matched.")

        exit = input("Would you like to play again? > ")
        if exit != "yes":
            break
main()