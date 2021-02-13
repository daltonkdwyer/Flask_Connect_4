import backend



G = backend.Game()
for i in range(10):
    game_won = G.play_game()
    print("Hello turn")
    print(G.B.turn_count)
    if G.B.turn_count == 6:
        G.reset()
    if game_won == 1:
        print("Game is won on front end")
