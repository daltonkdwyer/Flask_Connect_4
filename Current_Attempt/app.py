from flask import Flask, render_template, request
import game_class

app = Flask(__name__)

# Inputs: How many games, Player1 Type, Player 2 Type, Whether to print (0 = nothing, 1 = when game finished, 2 = every move)

# G = Game("Human", "Random", 2)
# winner_id, board_dict = Gi.play_game()

player_1_list =[5, 6, 7]
player_2_list = [30, 25]

@app.route('/', methods=["GET", "POST"])
def index():
    
    try:
        number = request.form.get("number")
    except:
        number = 404

    player_1_list.append(number)

    return render_template("index.html", number=number, player_1_list=player_1_list, player_2_list=player_2_list)


if __name__ == "__main__":
    app.run()
