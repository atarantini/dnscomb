====================================================================
Will build my own list of domains (distributed edition using Celery!
====================================================================


How I use it
============

Start one or more `Celery`_ workers:

.. code-block:: bash

    $ celery worker -A dnscomb -l info

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

And the worker should be checking if the domain exists:

.. code-block:: bash

    [2015-08-20 21:40:59,032: INFO/MainProcess] Received task: dnscomb.domain_exists[80e9f6bd-a837-409c-b282-0204abb73cbc]
    [2015-08-20 21:40:59,067: INFO/MainProcess] Task dnscomb.domain_exists[80e9f6bd-a837-409c-b282-0204abb73cbc] succeeded in 0.0337029579969s: False
    [2015-08-20 21:40:59,069: INFO/MainProcess] Received task: dnscomb.domain_exists[84fd6fff-0315-4db3-85ae-4bdb896e3660]
    [2015-08-20 21:40:59,098: INFO/MainProcess] Task dnscomb.domain_exists[84fd6fff-0315-4db3-85ae-4bdb896e3660] succeeded in 0.0278209769749s: False
    [2015-08-20 21:40:59,101: INFO/MainProcess] Received task: dnscomb.domain_exists[2152043e-3c1e-44e7-8af7-8424db981dbc]
    [2015-08-20 21:40:59,116: INFO/MainProcess] Task dnscomb.domain_exists[2152043e-3c1e-44e7-8af7-8424db981dbc] succeeded in 0.0139999679814s: False
    [2015-08-20 21:40:59,119: INFO/MainProcess] Received task: dnscomb.domain_exists[9c2666cf-db79-45fa-852c-c7c6417fc4e1]
    [2015-08-20 21:40:59,285: INFO/MainProcess] Task dnscomb.domain_exists[9c2666cf-db79-45fa-852c-c7c6417fc4e1] succeeded in 0.165478241979s: True


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
.. _Celery: https://http://www.celeryproject.org/