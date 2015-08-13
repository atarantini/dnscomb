"""
I want to build my own domain list by using a wordlist over a DNS server!
"""
import socket
import string
import argparse

import wordlist

TLD = ".com.ar"
MASK = "{name}{tld}"


def domain_exists(hostname):
    try:
        socket.gethostbyname(hostname)
        return True
    except Exception:
        pass

    return False


if __name__ == "__main__":
    # Parse CLI arguments
    parser = argparse.ArgumentParser(description='dnscomb will build my own list of domains!')
    parser.add_argument('--max', type=int, help='Maximum length of the domain name', default=3)
    parser.add_argument('--min', type=int, help='Minimum length of the domain name', default=1)
    args = parser.parse_args()

    generator = wordlist.Generator(string.ascii_lowercase)
    for name in generator.generate(args.min, args.max):
        hostname = MASK.format(
            name=name,
            tld=TLD
        )
        if domain_exists(hostname):
            print hostname