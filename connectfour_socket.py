# Leon Luong 69139013 and William Yam 71791723 Lab section 9

import socket
from collections import namedtuple

class ConnectFourProtocolError(Exception):
    pass

ConnectFourConnection = namedtuple('ConnectFourConnection', ['socket', 'input',
                                                             'output'])


_SHOW_DEBUG_TRACE = False


def connect(host: str, port: int) -> ConnectFourConnection:
    "Creates a sockets to communicate with ConnectFour Server"
    connectfour_socket = socket.socket()
    connectfour_socket.connect((host, port))
    connectfour_input = connectfour_socket.makefile('r')
    connectfour_output = connectfour_socket.makefile ('w')
    return ConnectFourConnection(socket = connectfour_socket,
                                 input = connectfour_input,
                                 output = connectfour_output)



def hello (connection: ConnectFourConnection, username: str) -> None:
    "Sends username, which follows I32CFSP protocol, to server"
    write_line(connection, 'I32CFSP_HELLO ' + username)
    response = read_line(connection)
    print(response)


def start_ai_game(connection: ConnectFourConnection) -> None:
    "Sends a line to start AI game with server"
    write_line(connection, "AI_GAME")
    response = read_line(connection)
    return response

def close(connection: ConnectFourConnection) -> None:
    "Closes sockets connect to server"
    connection.input.close()
    connection.output.close()
    connection.socket.close()



def read_line(connection: ConnectFourConnection) -> str:
    "Read a line sent by the server"
    line = connection.input.readline()[:-1]

    if _SHOW_DEBUG_TRACE:
        print('RCVD: ' + line)

    return line


def write_line (connection: ConnectFourConnection, line: str) -> None:
    "Immediately sends a line to the server"
    connection.output.write( line + '\r\n')
    connection.output.flush()
    if _SHOW_DEBUG_TRACE:
        print('SENT: ' + line)
