# 👑 Project 230: Golden Ticket Forger
**Type:** Active Directory Persistence
**Tech:** Kerberos Protocol

Demonstrates the logic of forging a Kerberos TGT (**Golden Ticket**). By compromising the `krbtgt` account hash, an attacker can create valid authentication tickets for non-existent users or grant themselves Domain Admin rights, persisting in the network for years undetected.