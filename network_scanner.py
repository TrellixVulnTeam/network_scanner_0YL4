#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    # print(arp_request.summary())

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()
    # print(broadcast.summary())

    # scapy.ls(scapy.Ether()) # list the variables of class

    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show() # more details
    # print(arp_request_broadcast.summary())

scan("10.0.2.2/24")