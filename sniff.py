#! /usr/bin/env python3

from scapy.all import sniff, TCP
import RSA

public, private = RSA.generate_keypair()

packets_seen = []

def custom_action(packet):
    payload = packet[0][1][TCP].payload
    if len(payload) == 0:
        return
    seq = packet[0][1][TCP].seq
    if seq in packets_seen:
        return
    packets_seen.append(seq)
    if packet[0][1].sport == 9999:
        indicator = "> "
    else:
        indicator = "< "
    return indicator + RSA.decrypt(bytes(payload), private)

sniff(filter="tcp", prn=custom_action, iface="lo", store=0)