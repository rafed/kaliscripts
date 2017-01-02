#!/bin/sh

iptables -t nat -F # --flush
iptables -F
