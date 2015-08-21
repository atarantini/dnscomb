"""
I want to build my own domain list by using a wordlist over a DNS server!
"""
import socket
import string
import argparse
from itertools import tee

import wordlist
from clint.textui import progress

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
    parser.add_argument('--resume', type=str, help='Resume list from the supplied domain name, optional. Example: aaa (will produce names staring in aab, aac, aad, etc)', default=None)
    parser.add_argument('--output', type=str, help='Save output into a file', default=None)
    args = parser.parse_args()

    wordlist_generator = wordlist.Generator(args.charset)
    if args.pattern:
        g = wordlist_generator.generate_with_pattern(args.pattern)
    else:
        g = wordlist_generator.generate(args.min, args.max)

    resume_ready = False
    g, g_count = tee(g)
    total = sum(1 for x in g_count)
    del g_count

    with progress.Bar(label="Resuming...", expected_size=total) as bar:
        val = 0
        last_val = 0
        for name in g:
            hostname = MASK.format(
                name=name,
                tld=args.tld
            )
            last_val = val
            val += 1
            if not resume_ready and args.resume:
                if name == args.resume:
                    resume_ready = True
                continue

            bar.label = hostname + " "
            bar.show(val)

            if domain_exists(hostname):
                if args.output:
                    f = file(args.output, "a")
                    f.write(hostname + u"\n")
                    f.close()
                    continue