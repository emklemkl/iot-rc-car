
from src.motor import Motor
from machine import Pin
import network
import usocket as socket
import time
# Server Connection Info
HOST = "192.168.1.8"
PORT = 3000

motor1 = Motor(Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4))
def start_server():
    # Server setup
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 3000))  # Bind to all interfaces on port 3000
    s.listen(1)  # Listen for 1 connection
    
    print("Server listening on port 3000")

    while True:
        conn, addr = s.accept()  # Accept a connection
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)  # Receive data from the client
            print(data.decode("utf-8"),"asdasdasddsa")
            if data.decode("utf-8") == "123":
                motor1.forward()
                time.sleep(2)
                motor1.stop()
            if not data:
                break  # Exit loop if no data
            conn.sendall(data)  # Echo back the received data
        conn.close()  # Close the connection

    s.close()  # Close the server socket

start_server()

# # Create connection
# s = socket.socket()
# s.connect((HOST, PORT))
# def send_data(msg):
#     s.send(msg.encode())
#     response = s.recv(1024).decode()
#     return response
 
# # Will print the server responses after each data request
# print(send_data('Hello,'))
# print(send_data('Server!'))

# # Close the connection socket between the device and the server
# # s.close()
