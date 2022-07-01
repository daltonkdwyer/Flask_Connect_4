# Make a list of sets?
# c_player_set = self.player_1_set

# check_set = {1, 8, 15, 23}
#
# win_list = []
# # A = Horizontal, B = Vertical, C = Diagonal Right, D = Diagonal Left
# win_possibilities = ["A", "B", "C", "D"]
# # Wincomb_dict Structure = [[starting moves], [add number, how many iterations on current row], [add number to get to next row, how many rows to try]]
# wincomb_dict = {'A': [[1,2,3,4], [1,4], [7,6]], 'B': [[1,8,15,22],[7,3],[1,7]], 'C': [[1,9,17,25],[1,4],[7,3]], 'D': [[4,10,16,22],[1,4],[7,3]]}
# for wp in win_possibilities:
#     y = 0
#     for j in range(wincomb_dict[wp][2][1]):
#         x = 0
#         for i in range(wincomb_dict[wp][1][1]):
#             win_set = set()
#             for k in range(4):
#                 win_set.add(wincomb_dict[wp][0][k]+x+y)
#             win_list.append(win_set)
#             # print(win_set)
#             # if all(item in c_player_set for item in win_set):
#                 # return 1
#             x = x + wincomb_dict[wp][1][0]
#         y = y + wincomb_dict[wp][2][0]
#
# return win_list
#
# # print(win_list)
# for set in win_list:
#     if all(item in check_set for item in set):
#         print("Got it!")

# i = "banana"
#
# if type(i) is not int:
#     i = 20
#
# print(int(i))

# player_ID = 2
# player_1_list = ["pinecone"]
# player_2_list = ["banana", "avocado"]
# fruit = "peach"
# print(player_ID)
#
# current_player_list = "player_" + str(player_ID) + "_list"
# print(current_player_list)
#
# current_player_list.append(fruit)


# a = 10
# def function():
#     if a > 5:
#         return a
#
# print(function()[0])

import sqlite3

db = sqlite3.connect()

print(db)
