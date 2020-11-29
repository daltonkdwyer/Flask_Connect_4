#
# my_list = [1,1,4,2,6]
#
# result = my_list.count(6)
#
# print(result)


class Test_Class():
    def __init__(self):
        self.game_board = {'a':1, 'b':2}

t = Test_Class()

print (t.game_board)

t.game_board = {'a': 17, 'b': 32}

print(t.game_board)
