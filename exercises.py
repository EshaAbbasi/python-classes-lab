class Game:
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def play_game(self):
        print("Shall we play a game?")
        while not self.winner and not self.tie:
            self.render()
            self.get_move()
            self.check_for_winner()
            if self.winner:
                break
            self.check_for_tie()
            if self.tie:
                break
            self.switch_turn()
        self.render()

    def print_board(self):
        b = self.board
        print(f"""
              A   B   C
          1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
              ----------
          2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
              ----------
          3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie:
            print("Tie game")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input("Enter a valid move (example: A1): ").lower()
            if move not in self.board:
                print("Invalid move, try again.")
                continue
            if self.board[move] is not None:
                print("That square is already taken. Try again.")
                continue
            self.board[move] = self.turn
            break

    def check_for_winner(self):
        b = self.board
        win_conditions = [
            ('a1', 'b1', 'c1'), ('a2', 'b2', 'c2'), ('a3', 'b3', 'c3'),
            ('a1', 'a2', 'a3'), ('b1', 'b2', 'b3'), ('c1', 'c2', 'c3'),
            ('a1', 'b2', 'c3'), ('a3', 'b2', 'c1')
        ]
        for x, y, z in win_conditions:
            if b[x] and b[x] == b[y] == b[z]:
                self.winner = b[x]
                return

    def check_for_tie(self):
        all_filled = all(value is not None for value in self.board.values())
        if all_filled and not self.winner:
            self.tie = True

    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'


game_instance = Game()
game_instance.play_game()
