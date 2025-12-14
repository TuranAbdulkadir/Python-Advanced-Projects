# ⛓️ Smart Contract Vulnerability Scanner

## Overview
A static analysis tool designed to detect **Reentrancy Attacks** in Ethereum Solidity smart contracts. This is the vulnerability responsible for the famous DAO hack (50M$ loss).

## Logic
It checks for the **Checks-Effects-Interactions** pattern violation. If a contract sends Ether *before* updating the user's balance, it flags a critical vulnerability.

## Run Status
✅ **SAFE:** Runs locally on text strings. No blockchain connection required.