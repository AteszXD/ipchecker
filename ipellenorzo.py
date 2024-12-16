import re

ipcim = input("Kérem adjon meg egy ip címet: ")
ip = re.split(r'[.:]+', ipcim)
ipv6kar = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
példa IP címek:
2001:db8:3333:4444:CCCC:DDDD:EEEE:FFFF./192.168.255.255
"""

def ervenyesitoipv4(ip):
    index = 0
    for i in range(len(ip)):
        if int(ip[index]) >= 0 and int(ip[index]) <= 255:
            index += 1
    if index == 4:
        return True
    return False

def ervenyesitoipv6(ip):
    index2 = 0
    ipjoined = ip.join(':')
    for karakter in range(len(ipjoined)):
        if karakter in ipv6kar:
            index2 += 1
    if index2 == 8:
        return True
    return False


if ervenyesitoipv4(ip) == True:
    print("Ez egy IPv4-es cím.")
elif ervenyesitoipv6(ip) == True:
    print("Ez egy IPv6-os cím.")
else:
    print("Ez nem egy érvényes IP cím.")