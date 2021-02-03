import random
import app

class Board():
    def __init__(self):
        self.move_list = []
        self.player_1_set = set()
        self.player_2_set = set()
        self.turn_count = 0

    def board_move(self, move):
        while move in self.move_list:
            move += 7
            if move > 42:
                return 0
        if self.turn_count % 2:
            self.player_2_set.add(int(move))
        else:
            self.player_1_set.add(int(move))

        self.move_list.append(int(move))
        self.turn_count += 1

        print('Move list: ' + str(self.move_list))
        print('Player 1 Set: ' + str(self.player_1_set))
        print('Turn count: ' + str(self.turn_count))
        print('')

    def check_win(self):
        if self.turn_count % 2:
            c_player_set = self.player_1_set
        else:
            c_player_set = self.player_2_set

        # A = Horizontal, B = Vertical, C = Diagonal Right, D = Diagonal Left
        win_possibilities = ["A", "B", "C", "D"]
        # Wincomb_dict Structure = [[starting moves], [add number, how many iterations on current row], [add number to get to next row, how many rows to try]]
        wincomb_dict = {'A': [[1,2,3,4], [1,4], [7,6]], 'B': [[1,8,15,22],[7,3],[1,7]], 'C': [[1,9,17,25],[1,4],[7,3]], 'D': [[4,10,16,22],[1,4],[7,3]]}
        for wp in win_possibilities:
            y = 0
            for j in range(wincomb_dict[wp][2][1]):
                x = 0
                for i in range(wincomb_dict[wp][1][1]):
                    win_set = set()
                    for k in range(4):
                        win_set.add(wincomb_dict[wp][0][k]+x+y)
                    if all(item in c_player_set for item in win_set):
                        return 1
                    x = x + wincomb_dict[wp][1][0]
                y = y + wincomb_dict[wp][2][0]

        if self.turn_count > 41:
            return 3
        else:
            return 0

class Player():
    def __init__(self, player_type, player_ID):
        self.player_type = player_type
        self.player_ID = player_ID

    def make_move(self):
        if self.player_type == 'Random':
            user_move = random.randint(1,7)
            print("Random Move: " + str(user_move))
            return int(user_move)

        if self.player_type == 'Human':
            user_move = int(input("Human Move: "))


class Game():
    def __init__(self):
        self.B = Board()
        self.P1 = Player('Random', 1)
        self.P2 = Player('Random', 2)
        game_won = 0

    # def play_game(self):
    #     while self.B.check_win() == 0:
    #         if self.B.turn_count % 2:
    #             c_player = self.P2
    #         else:
    #             c_player = self.P1
    #
    #         move = c_player.make_move()
    #         while self.B.board_move(move) == 0:
    #             move = c_player.make_move()
    #
    #         if self.B.check_win() == 1:
    #             print("Player " + str(c_player.player_ID) + " wins")
    #
    #     if self.B.check_win() == 3:
    #         print("Game Drawn!")
