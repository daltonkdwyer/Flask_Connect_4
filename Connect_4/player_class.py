import random
from board_class import Board

# takes a dictionary and decides which number to play, 1-7

class Player():
    def __init__(self, player_type, player_num):
        self.player_type = player_type
        player_piece_list = ['X', 'O']
        self.player_piece = player_piece_list[int(player_num) - 1]
        self.opposing_piece = ''
        if self.player_piece == 'X':
            self.opposing_piece = 'O'
        else: self.opposing_piece = 'X'
        self.player_num = player_num

    def make_move_master(self, board_dict):
        if self.player_type == 'Random':
            move = self.make_move_random()

        if self.player_type == 'Human':
            move = self.make_move_human()

        if self.player_type == 'Smart1':
            move = self.make_move_smart_1(board_dict)

        if self.player_type == 'Smart2':
            move = self.make_move_smart_2(board_dict)

        return move, self.player_piece

    def make_move_random(self):
        user_move = random.randint(1,7)
        return user_move

    def make_move_human(self):
        user_move = input("Make move: ")
        return int(user_move)

    def make_move_smart_1(self, board_dict):
        # Just checks if next move is winning, or blocks an opposing winning move
        temp_B = Board()
        temp_B.board_dict = board_dict.copy()

        for i in range(1, 8):
            temp_B.board_move(i, self.player_piece)
            if temp_B.is_win() is True:
                return i
            else: temp_B.board_dict = board_dict.copy()

        for i in range(1,8):
            temp_B.board_move(i, self.opposing_piece)
            if temp_B.is_win() is True:
                return i
            else: temp_B.board_dict = board_dict.copy()

        user_move = random.randint(1,7)
        return user_move

    def make_move_smart_2(self, board_dict):
        # Checks if can force a win
        win_count = 0

        temp_B = Board()
        temp_B.board_dict = board_dict.copy()

        for i in range(1,8):
            temp_B.board_dict = board_dict.copy()
            temp_B.board_move(i, self.player_piece)
            temp_B.print_board()
            for k in range(1,8):
                temp_B.board_move(k, self.opposing_piece)
                temp_B.print_board()
                for p in range(1,8):
                    print("Loop: " + str(i) + str(k) + str(p))
                    temp_B.board_move(p, self.player_piece)
                    temp_B.print_board()
                    if temp_B.is_win() is True:
                        print("Winning combo found!")
                        win_count += 1
                        if win_count == 7:
                            return i
                        break
                    else:
                        temp_B.take_back()
                temp_B.take_back()

        print("Random Move playing")
        user_move = random.randint(1,7)
        return user_move
