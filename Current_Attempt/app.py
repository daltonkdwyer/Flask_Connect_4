from flask import Flask, render_template, request
import backend

app = Flask(__name__)




G = backend.Game()

# player_1_set = G.B.player_1_set
# player_2_set = G.B.player_2_set

@app.route('/', methods=["GET", "POST"])
def index():

    human_move = request.form.get("number")
    while G.B.board_move(int(human_move)) == 0:
        human_move = request.form.get("number")

    if G.B.check_win() == 1:
        print("Someone won!")

    random_move = G.P2.make_move()
    while G.B.board_move(random_move) == 0:
        random_move = G.P2.make_move()

    if G.B.check_win() == 1:
        print("Someone won!")

    player_1_set = G.B.player_1_set
    player_2_set = G.B.player_2_set

    return render_template("index.html", player_1_list=player_1_set, player_2_list=player_2_set)

if __name__ == "__main__":
    app.run()


    # while G.B.check_win() == 0:
    #     if G.B.turn_count % 2:
    #         move = request.form.get("number")
    #         try:
    #             int(move)
    #         except:
    #             move = input('Make a move: ')
    #         G.B.board_move(move)
    #         # move = G.P2.make_move()
    #         # while G.B.board_move(move) == 0:
    #         #     move = G.P2.make_move()
    #     else:
    #         move = G.P1.make_move()
    #         while G.B.board_move(move) == 0:
    #             move = G.P1.make_move()
    #
    #     if G.B.check_win() == 1:
    #         # print("Player " + str(c_player.player_ID) + " wins")
    #         print("test")
    #
    # if G.B.check_win() == 3:
    #     print("Game Drawn!")





# player_move = request.form.get("number")


    # try:
    #     int(player_move)
    #     player_1_list.append(player_move)
    # except:
    #     player_move = 606
