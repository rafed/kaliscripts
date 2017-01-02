#!/bin/sh

iptables --table nat -A POSTROUTING --out-interface eth0 -j MASQUERADE
iptables -A FORWARD -j ACCEPT --in-interface at0

echo 1 > /proc/sys/net/ipv4/ip_forward

