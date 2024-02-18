# Player 1 = 1
# Player 2 = 2 

game = [[0, 0, 0], 
        [0, 0, 0], 
        [0, 0, 0], ]

# def player1_moves():
#         row, column  = input("Please enter your coordinates: ").split()
#         row = int(row)
#         column = int(column)
#         game[x][y] = 1
# player1_moves()

def game_board(game_map, player=0, row=0, column=0, just_display=False):
        print("   0  1  2")
        if not just_display:
                game_map[row][column] = player
        for count, row in enumerate(game_map):
                print(count, row)

        return game_map

game = game_board(game, just_display=True)
game = game_board(game, player=1, row=2, column=1)



