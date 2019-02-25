import socket


def setup_server():
    echo_server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP)
    echo_server.bind(('127.0.0.1', 4444))
    echo_server.listen(1)
    return echo_server, echo_server.accept()


if __name__ == '__main__':
    server, (conn, addr) = setup_server()
    print('Received client connection for {}'.format(addr))

    buffer_length = 16
    message_complete = False

    while not message_complete:
        part = conn.recv(buffer_length)
        print(part.decode())
        if len(part) < buffer_length:
            break

    message = 'The server received your message!'
    conn.sendall(message.encode())

    conn.close()
    server.close()
