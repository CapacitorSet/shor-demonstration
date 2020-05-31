import logging
import RSA
import socketserver

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)

public, private = RSA.generate_keypair(3, 11)

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        logging.info("New connection from {}".format(self.client_address[0]))

        # Send the public key
        pubkey_message = "pubkey: e={}, n={}".format(public[0], public[1])
        logging.debug("Sent: {}".format(pubkey_message))
        self.request.sendall(bytes(pubkey_message, 'utf-8'))

        # Read the username and discard it
        self.request.recv(1024)
        # Read the password and discard it
        self.request.recv(1024)

        output = RSA.encrypt("henlo", public)
        logging.debug("Sent: {}".format(output))
        self.request.sendall(output)
        self.request.close()

HOST, PORT = "localhost", 9999

# Create the server, binding to localhost on port 9999
with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
    logging.info("Listening on {}".format(HOST, PORT))
    server.serve_forever()