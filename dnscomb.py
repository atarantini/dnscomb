"""
I want to build my own domain list by using a wordlist over a DNS server!
"""
import socket
import string

import wordlist


def domain_exists(hostname):
    try:
        socket.gethostbyname(hostname)
        return True
    except Exception:
        pass

    return False


TLD = ".com.ar"
MASK = "{name}{tld}"

generator = wordlist.Generator(string.ascii_lowercase)
for name in generator.generate(1, 3):
    hostname = MASK.format(
        name=name,
        tld=TLD
    )
    if domain_exists(hostname):
        print hostname