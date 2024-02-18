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

def game_board(player=0, row=0, column=0, just_display=False):
        print("   1  2  3")

        if not just_display:
                game[row][column] = player
        for count, row in enumerate(game):
                print(count, row)

game_board(just_display=True)


