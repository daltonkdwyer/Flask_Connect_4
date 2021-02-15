from flask import Flask, render_template, request
import backend

app = Flask(__name__)

G = backend.Game()

@app.route('/', methods=["GET", "POST"])
def index():

    game_won = G.play_game()

    if game_won is not None:
        win_set = game_won[1]
        if game_won[0] == 1:
            return render_template('endgame.html', player_1_list=G.B.player_1_set, player_2_list=G.B.player_2_set, win_set=win_set, possible_move_list=G.B.possible_move_list)
        if game_won[0] == 3:
            return "Game Drawn"

    return render_template("index.html", player_1_list=G.B.player_1_set, player_2_list=G.B.player_2_set, possible_move_list=G.B.possible_move_list)

@app.route('/endgame', methods=["GET", "POST"])
def endgame():
    if request.form.get("submit_button") == 'Restart Game':
        G.reset()
        return render_template("index.html", player_1_list=G.B.player_1_set, player_2_list=G.B.player_2_set, possible_move_list=G.B.possible_move_list)

    return render_template("endgame.html")


if __name__ == "__main__":
    app.run()
