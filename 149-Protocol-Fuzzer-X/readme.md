# 🔨 Smart Protocol Fuzzer

## Overview
A generation-based fuzzer. Unlike "dumb" fuzzers that send random noise, this tool understands protocol states (like FTP or HTTP) and injects specific attack vectors (Buffer Overflow, Format String) into valid command structures.

## Run Status
✅ **SAFE:** Generates strings locally. Does not flood network unless modified.