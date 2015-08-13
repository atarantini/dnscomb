"""
I want to build my own domain list by using a wordlist over a DNS server!
"""
import socket
import string
import argparse

import wordlist

TLD = ".com"
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
    parser.add_argument('--tld', type=str, help='Top-level domain, default: .com', default=TLD)
    parser.add_argument('--charset', type=str, help='Charset for the wordlist, default: abcdefghijklmnopqrstuvwxyz', default=string.ascii_lowercase)
    parser.add_argument('--pattern', type=str, help='Wordlist pattern, optional. Example: examp@e (will produce: exampae, exampbe, exampce, etc)', default=None)
    args = parser.parse_args()

    wordlist_generator = wordlist.Generator(args.charset)
    if args.pattern:
        g = wordlist_generator.generate_with_pattern(args.pattern)
    else:
        g = wordlist_generator.generate(args.min, args.max)

    for name in g:
        hostname = MASK.format(
            name=name,
            tld=args.tld
        )
        if domain_exists(hostname):
            print hostname