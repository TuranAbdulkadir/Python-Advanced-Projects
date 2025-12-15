# 💣 Project 178: Zero-Day Fuzzer
**Type:** Exploit Development  
**Tech:** Socket Programming, Fuzzing Logic

## Description
An automated **Fuzzer** designed to stress-test network services (like FTP, HTTP, SSH). 
It sends incrementally larger buffers of junk data ("A" characters) to specific inputs. If the target service crashes, it indicates a potential **Buffer Overflow** vulnerability, which is the first step in creating a Zero-Day exploit.