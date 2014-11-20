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

.. code:: bash
    $ pip install snorse

Usage
-----

Command Line

.. code:: bash
    $ snorse snowman
    ☃ ☃ ☃   ⛄⛄⛄ ☃   ⛄⛄⛄ ⛄⛄⛄ ⛄⛄⛄   ☃ ⛄⛄⛄ ⛄⛄⛄   ⛄⛄⛄ ⛄⛄⛄   ☃ ⛄⛄⛄   ⛄⛄⛄ ☃


Python

.. code:: python
    >>> import snorse
    >>> snorse.snorse('snowman')
    u'\u2603 \u2603 \u2603   \u26c4\u26c4\u26c4 \u2603   \u26c4\u26c4\u26c4 \u26c4\u26c4\u26c4 \u26c4\u26c4\u26c4   \u2603 \u26c4\u26c4\u26c4 \u26c4\u26c4\u26c4   \u26c4\u26c4\u26c4 \u26c4\u26c4\u26c4   \u2603 \u26c4\u26c4\u26c4   \u26c4\u26c4\u26c4 \u2603'
    >>> print snors.snorse('snowman')
    ☃ ☃ ☃   ⛄⛄⛄ ☃   ⛄⛄⛄ ⛄⛄⛄ ⛄⛄⛄   ☃ ⛄⛄⛄ ⛄⛄⛄   ⛄⛄⛄ ⛄⛄⛄   ☃ ⛄⛄⛄   ⛄⛄⛄ ☃


Profit!
