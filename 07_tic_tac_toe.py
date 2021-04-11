import random
import time

class Player:

    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        val = None
        valid_square = False
        while not valid_square:
            square = input(self.letter + '\'s turn'
                                         ' input move 0-9')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid move, please select a valid option")
        return val


class TicTacToe:

    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.current_winner = None

    def print_status_board(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' | ')

    @staticmethod
    def print_board_values():
        number_board = [[str(i) for i in range(j*3 , (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' | ')

    def empty_squares(self):
        return ' ' in self.board

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, letter, square):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(letter, square):
                self.current_winner = letter
            return True
        return False


    def winner(self, letter, square):

        row_index = square//3
        row = self.board[row_index*3: (row_index+1)*3]
        if all([spot == letter for spot in row]):
            return True
        column_index = square % 3
        column = [self.board[column_index+(i*3)] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in (0, 4, 8)]
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in (2, 4, 6)]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def play(game, o_player, x_player, print_game = True):

    if print_game:
        game.print_board_values()

    letter = 'X'

    while game.empty_squares():

        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(letter, square):
            if print_game:
                print(letter + f' has made move to {square}')
                game.print_status_board()
                print(' ')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins')

                return letter

            letter = 'O' if letter == 'X' else 'X'

        time.sleep(0.9)

    if print_game:
        print('It\'s a tie')

if __name__ == '__main__':

    o_player = RandomComputerPlayer('O')
    x_player = HumanPlayer('X')
    t = TicTacToe()
    play(t, o_player, x_player, print_game=True)























