import itertools

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
                if game_map[row][column] != 0:
                        print("This position is taken! Chose another")
                        return game_map, False 
                print("   0  1  2")
                if not just_display:
                        game_map[row][column] = player
                for count, row in enumerate(game_map):
                        print(count, row)
                return game_map, True 

                return game_map
        except IndexError as e:
                print("Error: make sure you input row/ column as 0, 1 or 2?", e)
                return game_map, False
        except Exception as e:
                print("Something went very wrong!", e)
                return game_map, False

play = True
players = [1, 2]
while play:
        game = [[0, 0, 0], 
                [0, 0, 0], 
                [0, 0, 0]]
        
        game_won = False
        player_choice = itertools.cycle([1, 2])
        game, _ = game_board(game, just_display=True)
        while not game_won:
                current_player = next(player_choice)
                print(f"Current Player: {current_player}")
                played = False

                while not played:
                        column_choice = int(input("What column do you want to play? (0, 1, 2): "))
                        row_choice = int(input("What row do you want to play? (0, 1, 2): "))
                        game, played = game_board(game, current_player, row_choice, column_choice)