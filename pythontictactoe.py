# Player 1 = 1
# Player 2 = 2 

game = [[1, 0, 1], 
        [0, 1, 0], 
        [2, 2, 1], ]

# ways to win

def win(current_game):
        # - Horizontally
        for row in game:
                print(row)
                if row.count(row[0]) == len(row) and row[0] != 0:
                        print("winner! - horizontal Win!")

        # | Vertically
        for col in range(len(game[0])):
                check = []

                for row in game:    
                        check.append(row[col])
                if check.count(check[0]) == len(check) and check[0] != 0:
                        print("winner! | Vertical Win!")

        # / Diagonally 
        diags = []              
        for idx, reverse_idx in enumerate(reversed(range(len(game)))):
                diags.append(game[idx][reverse_idx])
        if diags.count(diags[0]) ==  len(diags) and diags[0] != 0:
                print("winner! / diagonal win!")

        # \ Diagonally
        diags = []
        for ix in range(len(game)):
                diags.append(game[ix][ix])
        if diags.count(diags[0]) == len(diags) and diags[0] != 0:
                print("winner! \\ diagonal win!")      


def game_board(game_map, player=0, row=0, column=0, just_display=False):
        try:
                print("   0  1  2")
                if not just_display:
                        game_map[row][column] = player
                for count, row in enumerate(game_map):
                        print(count, row)

                return game_map
        except IndexError as e:
                print("Error: make sure you input row/ column as 0, 1 or 2?", e)
        except Exception as e:
                print("Something went very wrong!", e)

game = game_board(game, just_display=True)
game = game_board(game, player=1, row=1, column=1)