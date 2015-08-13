==================================
Will build my own list of domains!
==================================

How I use it
============

Build a simple list:

.. code-block:: bash

    $ python dnscomb.py --tld .com.ar --min 1 --max 2 > domains-com-ar-a-zz.db


Resulting file should look like::

    $ head domains-com-ar-a-zz.db
    a.com.ar
    c.com.ar
    d.com.ar
    e.com.ar
    f.com.ar
    g.com.ar
    h.com.ar
    i.com.ar
    j.com.ar
    l.com.ar
    $ tail domains-com-ar-a-zz.db
    wd.com.ar
    wr.com.ar
    xl.com.ar
    xp.com.ar
    ya.com.ar
    za.com.ar
    zc.com.ar
    ze.com.ar
    zg.com.ar
    zv.com.ar


Help
====

.. code-block:: bash

    $ python dnscomb.py -h
    usage: dnscomb.py [-h] [--max MAX] [--min MIN] [--tld TLD] [--charset CHARSET]

    dnscomb will build my own list of domains!

    optional arguments:
      -h, --help         show this help message and exit
      --max MAX          Maximum length of the domain name
      --min MIN          Minimum length of the domain name
      --tld TLD          Top-level domain, default: .com
      --charset CHARSET  Charset for the wordlist, default: abcdefghijklmnopqrstuvwxyz
      --pattern PATTERN  Wordlist pattern, optional. Example: examp@e (will
                         produce: exampae, exampbe, exampce, etc)
      --resume RESUME    Resume list from the supplied domain name, optional.
                         Example: aaa (will produce names staring in aab, aac,
                         aad, etc)

For more examples about ``--pattern`` see `rexos/wordlist`_ documentation: it's
an amazing library!

NSFAQ
=====

Is this the better/faster/efficient/whatever way to get a list of domains?
--------------------------------------------------------------------------

NO, but it works and is simple.

What I can do with this script?
-------------------------------

Some ideas:

* Create your own domain database :)
* Find registered or non-registered domains :)
* Stress your DNS server :)
* :) :) :)

.. _rexos/wordlist: https://github.com/rexos/wordlist/blob/master/README.md