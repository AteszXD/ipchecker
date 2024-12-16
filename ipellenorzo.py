import re

ipcim = input("Kérem adjon meg egy ip címet: ")
ip = re.split(r'[.:]+', ipcim)
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
    index = 0
    for i in range(len(ip)):
        if ip[index] >= 0 and ip[index] <= 255:
            index += 1
    if index == 8:
        return True
    return False


if ervenyesitoipv4(ip) == True:
    print("Ez egy IPv4-es cím.")
elif ervenyesitoipv6(ip) == True:
    print("Ez egy IPv6-os cím.")
else:
    print("Ez nem egy érvényes IP cím.")