

.. towncrier release notes start

Falsifier 1.0 (2024-12-15)
==========================

Features
--------

- Add ``Falsifier`` base class for creating objects that evaluate to ``False`` in
  boolean contexts. Each instance has a unique identity, supports proper equality
  comparison and hashing, and can be used in collections like sets and
  dictionaries.


Supported Platforms
-------------------

- Add support for CPython 3.10 to 3.13.
- Add support for PyPy 3.10.
