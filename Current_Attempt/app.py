from flask import Flask, render_template, request
import backend

app = Flask(__name__)

G = backend.Game()
print(G.B.player_1_set)

@app.route('/', methods=["GET", "POST"])
def index():

    G.play_game()

    player_1_set = G.B.player_1_set
    player_2_set = G.B.player_2_set

    return render_template("index.html", player_1_list=player_1_set, player_2_list=player_2_set)

@app.route('/endgame')
def endgame():

    return render_template("endgame.html")


if __name__ == "__main__":
    app.run()
