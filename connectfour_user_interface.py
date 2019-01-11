# Leon Luong 69139013 and William Yam 71791723 Lab section 9

import connectfour_functions
import connectfour_console
import connectfour_socket
import connectfour
import time


     


def connect_to_server() -> None:
    "Forms connections to server"
    while True:
        try:
            host = connect_host()
            port = connect_port()
            username = choose_username()
            connection = connectfour_socket.connect(host, port)
            connectfour_socket.hello(connection, username)
            start = connectfour_socket.start_ai_game(connection)
            if start == "READY":
                print('Okay! Starting game.')
                print()
                return connection
            elif start == "END":
                print('Goodbye.')
                sys.exit()
        except connectfour_socket.ConnectFourProtocolError:
            print ("Invalid host or port. Please try again.")
        except OSError:
            print("Invalid host or port. Please try again.")



def choose_username() -> str:
    "Asks user to submit valid username and returns it"
    while True:
        username = input("Please input a one-word username: ")
        if len(username.split()) > 1:
            print("Invalid username. Please try again.")
            pass
        else:
            return username


def connect_port () -> int:
    "Asks user to submit valid port and returns it"
    while True:
        try: 
            port = int(input("What port would you like to connect to: "))
            if port < 0 or port > 65535:
                print("Invalid port number. Please choose a port between 0 and 65535")
            else:
                return port
        except ValueError:
            print("Please input a number for the port.")
        

def connect_host () -> str:
    "Asks user to submit valid host and returns it"
    host = str(input("What host would you like to connect to: "))
    return host



def ai_introduction():
    "Prints a welcome banner and the rules of Connect Four."
    print("Welcome to Connect Four!")
    print()
    print("INSTRUCTIONS: type drop/pop and the number of the column "
          "you want to place or remove a chip. \nExample: drop 4 or pop 7")
    print("First to have four chips in a row wins!")
    print("You are (R)ed")
    print("The AI is (Y)ellow")
    print()

    

def send_move(connection: connectfour_socket.ConnectFourConnection) -> tuple or None:
    "Sends valid move to server and returns response."
    while True:
        try:
            choice = input("Please make your move: ")
            choice_option = choice.split()[0].upper()
            check_choice(choice_option)
            column = choice.split()[1]
            check_column(column)
            user_move = (choice_option + ' ' + column)  
            connectfour_socket.write_line(connection, user_move)
            response = connectfour_socket.read_line(connection)
            if response == "OKAY":
                ai_response = connectfour_socket.read_line(connection)
                ai_ready = connectfour_socket.read_line(connection)
                turn = (user_move, ai_response, ai_ready)
                return turn
            elif response == "INVALID":
                print("Invalid move, please try again.")
                ai_ready = connectfour_socket.read_line(connection)
            elif response == "WINNER_RED":
                print("Congratulations! You have won!")
                return
        except ValueError:
            print("Invalid move, please pick a valid column number.")
        except IndexError:
            print("Invalid move. Please try again.")
        except connectfour.InvalidMoveError:
            print("Invalid move, please do a different move.")


def check_choice(choice_option: str):
    "Checks to see if user is making a valid move."
    if choice_option == 'DROP':
        pass
    elif choice_option == 'POP':
        pass
    else:
        raise connectfour.InvalidMoveError

def check_column(column: str):
    "Checks to see if user chose a valid column."
    if type(int(column)) == int:
        pass
    else:
        raise ValueError



            
def winner_display (response: str) -> None:
    "Checks the response to see if RED or YELLOW has won"
    if response == "WINNER_YELLOW":
        print("Game over. The AI has won.")
    else:
        pass


def closing_display (connection: 'ConnectFourConnection') -> None:
    "Shows closing message after game ends."
    print()
    print("Thanks for playing")
    print("This program will close after 10 seconds")
    print()
    time.sleep(10)
    connectfour_socket.close(connection)
    return
    
    

def start_game_session(connection: 'ConnectFourConnection') -> None:
    "Starts game and submits turns back and forth until game ends."
    game_state = connectfour.new_game()
    while True:
        turns = send_move(connection)
        if turns == None:
            closing_display(connection)
            break
        game_state = connectfour_functions.make_move(game_state, turns[0])
        print("\nThe AI has made its move!\n")
        game_state = connectfour_functions.make_move(game_state, turns[1])
        connectfour_functions.show_game_board(game_state, connectfour.BOARD_COLUMNS, connectfour.BOARD_ROWS)   
        if turns[2] != "READY":
            winner_display(turns[2])
            closing_display(connection)
            break




if __name__ == '__main__':
    server = connect_to_server()
    ai_introduction()
    start_game_session(server)

