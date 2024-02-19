import itertools

def win(current_game):

        def all_same(l):
                if l.count(l[0]) == len(l) and l[0] != 0:
                        return True 
                else:
                        return False 
        # - Horizontally
        for row in game:
                print(row)
                if all_same(row):
                        print("winner! - horizontal Win!")
                        return True

        # | Vertically
        for col in range(len(game[0])):
                check = []

                for row in game:    
                        check.append(row[col])
                if all_same(check):
                        print("winner! | Vertical Win!")
                        return True

        # / Diagonally 
        diags = []              
        for idx, reverse_idx in enumerate(reversed(range(len(game)))):
                diags.append(game[idx][reverse_idx])
        if all_same(diags):
                print("winner! / diagonal win!")
                return True

        # \ Diagonally
        diags = []
        for ix in range(len(game)):
                diags.append(game[ix][ix])
        if all_same(diags):
                print("winner! \\ diagonal win!")
                return True     
        
        return False 

def game_board(game_map, player=0, row=0, column=0, just_display=False):

        try:
                # Stops the users from playing over eachother
                if game_map[row][column] != 0:
                        print("This position is taken! Chose another")
                        return game_map, False 
                # Creating a dynamic board size, the user can specify any board size
                print("   "+"  ".join([str(i) for i in range(len(game_map))]))
                if not just_display:
                        game_map[row][column] = player
                for count, row in enumerate(game_map):
                        print(count, row)
                return game_map, True 

        except IndexError as e:
                print("Error: make sure you input row/ column as 0, 1 or 2?", e)
                return game_map, False
        except Exception as e:
                print("Something went very wrong!", e)
                return game_map, False

play = True
players = [1, 2]
while play:
        game_size = int(input("What size game of tic tac toe? "))
        game = [[0 for i in range(game_size)] for i in range(game_size)]
        game_won = False
        player_cycle = itertools.cycle([1, 2]) # Cycles between player 1 and 2 / alternates between the two
        game, _ = game_board(game, just_display=True)
        while not game_won:
                current_player = next(player_cycle)
                print(f"Current Player: {current_player}") # Shows the current player
                played = False
                while not played:
                        # Takes user input for the coordinates for the game. 
                        column_choice = int(input("What column do you want to play? (0, 1, 2): "))
                        row_choice = int(input("What row do you want to play? (0, 1, 2): "))
                        game, played = game_board(game, current_player, row_choice, column_choice)

                if win(game):
                        # After the game ends or a player wins, the user can choose to play again or quit.
                        game_won = True
                        again = input("The game is over, would you like to play again? (yes/ no): ")
                        if again.lower() == "yes":
                                print("Restarting... ...")
                        elif again.lower() == "no":
                                print("Quitting... ...")
                                play = False 
                        else:
                                print("Not a valid answer, retry.")
                                play = False