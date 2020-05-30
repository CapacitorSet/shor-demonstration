import socket
import sys
import RSA

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

public, private = RSA.generate_keypair()

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    msg = data
    encrypted_msg = RSA.encrypt(msg, public)
    sock.sendall(bytes(encrypted_msg))
    # sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    indata = sock.recv(1024)
    received = str(indata, "utf-8")
    decrypted = RSA.decrypt(indata, private)
    # received = RSA.decrypt(encrypted_msg, private)

print("Sent:     {}".format(data))
print("Received: {}".format(decrypted))