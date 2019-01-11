# Leon Luong 69139013 and William Yam 71791723 Lab section 9


import connectfour
import connectfour_functions



def console_gameplay(game_state: 'GameState') -> 'GameState':
    "Takes a player's input and performs that action. Then, changes turns."
    while True:
        try:
            if game_state.turn == connectfour.RED:
                print()
                print("It is now Red player's turn.")
                print()
            elif game_state.turn == connectfour.YELLOW:
                print()
                print("It is now Yellow player's turn.")
                print()
            choice = input("Please make your move: ")
            game_state = connectfour_functions.make_move(game_state, choice)
            return game_state
        except connectfour.InvalidMoveError:
            print("Invalid move, please do a different move.")
        except ValueError:
            print("Invalid move, please pick a valid column number.")
        except IndexError:
            print("Invalid move.")





def introduction():
    "Prints a welcome banner and the rules of Connect Four."
    print("Welcome to Connect Four!")
    print()
    print("INSTRUCTIONS: The first player is (R)ed and the second player is (Y)ellow.\n Type drop/pop and the number of the column "
          "you want to place or remove a chip. \nExample: drop 4 or pop 7")
    print("First to have four chips in a row wins!")
    print()



def winner_banner(game_state: 'GameState'):
    "Prints a message if a player has won or else it does nothing."
    if connectfour.winner(game_state) == connectfour.RED:
        print ("The game is over. Red player won!")
        pass
    elif connectfour.winner(game_state) == connectfour.YELLOW:
        print ("The game is over. Yellow player won!")
        pass
    else:
        pass

    

        
if __name__ == '__main__':
    introduction()
    game_state = connectfour.new_game()
    while True:
        game_state = console_gameplay(game_state)
        connectfour_functions.show_game_board(game_state, connectfour.BOARD_COLUMNS, connectfour.BOARD_ROWS)
        if connectfour.winner(game_state) != connectfour.NONE:
            winner_banner(game_state)
            break

