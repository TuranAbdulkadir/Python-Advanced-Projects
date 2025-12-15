# ☁️ Project 196: Cloud Bucket Hunter
**Type:** Cloud Security / Recon  
**Tech:** Requests, AWS S3 API

## Description
Scans for misconfigured **AWS S3 Buckets**.
Many organizations accidentally leave cloud storage buckets public. This tool brute-forces bucket names based on keywords and checks if they are accessible (HTTP 200), potentially revealing sensitive corporate data.