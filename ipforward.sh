#!/bin/sh

echo -n "Previously: "; cat  /proc/sys/net/ipv4/ip_forward
echo 1 > /proc/sys/net/ipv4/ip_forward
echo -n "Now: "; cat  /proc/sys/net/ipv4/ip_forward
