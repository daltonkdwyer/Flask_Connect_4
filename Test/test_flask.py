import flask

def multiply_by_two(test_var):
    new_var = test_var * 2


TEXT = '''
<!doctype html>
<html>
    <head><title>Tic Tac Toe</title></head>

    <body>
        <input type="text" name="a" value="a">
        <input type="submit" value="Submit">


    </body>

</html>
'''


app = Flask(__name__)
global_number = ''

@app.route("/", methods=["GET", "POST"])
def index():
    global_number = ''
    test_var = request.form.get("number")


if __name__ == "__main__":
    app.run()
