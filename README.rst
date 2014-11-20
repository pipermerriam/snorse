===============================
Snorse
===============================

.. image:: https://badge.fury.io/py/snorse.png
    :target: http://badge.fury.io/py/snorse

.. image:: https://travis-ci.org/pipermerriam/snorse.png?branch=master
        :target: https://travis-ci.org/pipermerriam/snorse

.. image:: https://pypip.in/d/snorse/badge.png
        :target: https://pypi.python.org/pypi/snorse


Unicode Snowman Morse Code

* Free software: MIT license


Install
-------

.. code-block:: bash

    $ pip install snorse

Usage
-----

Command Line

.. code-block:: bash

    $ snorse snowman
    ☃ ☃ ☃   ⛄⛄⛄ ☃   ⛄⛄⛄ ⛄⛄⛄ ⛄⛄⛄   ☃ ⛄⛄⛄ ⛄⛄⛄   ⛄⛄⛄ ⛄⛄⛄   ☃ ⛄⛄⛄   ⛄⛄⛄ ☃
    $ cat snowman | snorse
    ☃ ☃ ☃   ⛄⛄⛄ ☃   ⛄⛄⛄ ⛄⛄⛄ ⛄⛄⛄   ☃ ⛄⛄⛄ ⛄⛄⛄   ⛄⛄⛄ ⛄⛄⛄   ☃ ⛄⛄⛄   ⛄⛄⛄ ☃
    $ echo snowman > snowman.txt
    $ snorse snowman.txt
    ☃ ☃ ☃   ⛄⛄⛄ ☃   ⛄⛄⛄ ⛄⛄⛄ ⛄⛄⛄   ☃ ⛄⛄⛄ ⛄⛄⛄   ⛄⛄⛄ ⛄⛄⛄   ☃ ⛄⛄⛄   ⛄⛄⛄ ☃
    $ snorse -f snowman.txt
    ☃ ☃ ☃   ⛄⛄⛄ ☃   ⛄⛄⛄ ⛄⛄⛄ ⛄⛄⛄   ☃ ⛄⛄⛄ ⛄⛄⛄   ⛄⛄⛄ ⛄⛄⛄   ☃ ⛄⛄⛄   ⛄⛄⛄ ☃
    

Python API

.. code-block:: python

    >>> import snorse
    >>> snorse.snorse('snowman')
    u'\u2603 \u2603 \u2603   \u26c4\u26c4\u26c4 \u2603   \u26c4\u26c4\u26c4 \u26c4\u26c4\u26c4 \u26c4\u26c4\u26c4   \u2603 \u26c4\u26c4\u26c4 \u26c4\u26c4\u26c4   \u26c4\u26c4\u26c4 \u26c4\u26c4\u26c4   \u2603 \u26c4\u26c4\u26c4   \u26c4\u26c4\u26c4 \u2603'
    >>> print snors.snorse('snowman')
    ☃ ☃ ☃   ⛄⛄⛄ ☃   ⛄⛄⛄ ⛄⛄⛄ ⛄⛄⛄   ☃ ⛄⛄⛄ ⛄⛄⛄   ⛄⛄⛄ ⛄⛄⛄   ☃ ⛄⛄⛄   ⛄⛄⛄ ☃


Profit!
