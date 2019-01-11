# Leon Luong 69139013 and William Yam 71791723 Lab section 9

import connectfour



def make_move(game_state:'GameState', choice: str) -> 'GameState':
        "Submits a valid move."
        choice_option = choice.split()[0]
        column_number = int(choice.split()[1]) - 1
        if choice_option.upper() == 'DROP':
                return connectfour.drop(game_state, column_number)
        elif choice_option.upper() == 'POP':
                return connectfour.pop(game_state, column_number)
        else:
                raise connectfour.InvalidMoveError



def show_game_board(game_state: 'GameState', columns: int, rows: int) -> list:
    "Shows the game board for users to see."
    result = []
    column_list = []
    for column_num in range(columns):
        column_list.append(str(column_num+1))
    for row in range(rows):
        result.append([])
        for column in range(columns):
            if game_state.board[column][row] == connectfour.NONE:
                result[row].append('.')
            if game_state.board[column][row] == connectfour.RED:
                result[row].append('R')
            if game_state.board[column][row] == connectfour.YELLOW:
                result[row].append('Y')
    print(" ".join(column_list))
    for row in result:
        print(" ".join(row))

