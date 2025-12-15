# 📦 Project 238: Repo Jacker (Supply Chain Attack)
**Type:** Global Scale Attack
**Tech:** Python Packaging (PyPI)

**Risk Level:** GLOBAL EPIDEMIC
Simulates a **Supply Chain Attack** via Typosquatting.
The attacker publishes a malicious package to a repository (like PyPI or NPM) with a name similar to a popular library. When developers make a typo and install it, the `setup.py` script executes immediately, compromising the developer's machine and potentially the software they are building for millions of users.