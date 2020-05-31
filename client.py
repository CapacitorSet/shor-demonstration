import logging
import re
import RSA
import socket
import sys

HOST, PORT = "localhost", 9999
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)

public, private = RSA.generate_keypair(3, 11)
pubkey_pattern = re.compile("pubkey: e=([0-9]+), n=([0-9]+)")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    logging.info("Connected to {}:{}".format(HOST, PORT))

    # Receive and parse pubkey
    pubkeydata = sock.recv(1024)
    pubkey_matches = pubkey_pattern.match(str(pubkeydata, 'utf-8'))
    pubkey = (int(pubkey_matches.group(1)), int(pubkey_matches.group(2)))
    logging.debug("Public key: {}".format(pubkey))

    print("Enter your credentials to log in.")
    print("")

    msg = input("    Email: ")
    encrypted_msg = RSA.encrypt(msg, pubkey)
    logging.debug("Sent {}".format(encrypted_msg))
    sock.sendall(encrypted_msg)
    msg = input("    Password: ")
    encrypted_msg = RSA.encrypt(msg, pubkey)
    logging.debug("Sent {}".format(encrypted_msg))
    sock.sendall(encrypted_msg)
    print("")
    print("Logged in successfully! Here are your emails:")
    print("")

    # Receive data from the server and shut down
    indata = sock.recv(1024)
    decrypted = RSA.decrypt(indata, private)
    logging.debug("Received {}".format(decrypted))