# This is a sample Python script.
import socket

# Press the green button in the gutter to run the script.
def handleGet(split):
    print(f"handle GET {split}")
    headers = getHeaders(split)


def handleHead(split):
    pass


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
                    # print(data)
                    split = data.decode().split("\r\n")
                    httpmethod = split[0].split(" ")[0]
                    print(httpmethod)
                    if "GET" == httpmethod:
                        handleGet(split)
                    elif "HEAD" == httpmethod:
                        handleHead(split)
                    # print(split)
                    # data_decode = data.decode()
                    #
                    # print(data_decode)
                    # print(type(data_decode))
                    #HEAD
                    conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 14\r\nLast-Modified: Sun, 18 Jun 2023 00:00:00 GMT\r\nContent-Type: text/plain\r\n\r\nthis is a body\r\n")

                    #GET
                    # conn.sendall(data)
                    # conn.sendall(b"HTTP/1.1 200 OK\r\n\r\nThis is the body\r\n\r\n")
                    # conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n")


def getHeaders(split) -> dict:
    headerfield = True
    i = 1
    headers = {}
    while headerfield:
        i_ = split[i]
        print(i_)
        if i_ == '':
            headerfield = False
            break
        i+=1
        keyValue = i_.split(": ", 1)
        headers[keyValue[0]] = keyValue[1]
    print(headers)
    return headers


