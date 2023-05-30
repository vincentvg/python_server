# This is a sample Python script.
import socket

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("startup socket")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 8080))
        s.listen()
        print("started listening")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(2048)
                if data:
                    print(data)
                    #HEAD
                    # conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 20354\r\nLast-Modified: Sun, 18 Jun 2023 00:00:00 GMT\r\nContent-Type: text/html\r\n\r\n")

                    #GET
                    # conn.sendall(data)
                    conn.sendall(b"HTTP/1.1 200 OK\r\n\r\nThis is the body\r\n\r\n")
                    # conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
