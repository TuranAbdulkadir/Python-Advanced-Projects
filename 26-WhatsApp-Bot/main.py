import pywhatkit
import datetime

print("--- WhatsApp Auto Sender ---")
number = input("Enter number (+905...): ")
msg = input("Enter message: ")
hour = int(input("Hour (24h): "))
minute = int(input("Minute: "))

print("Scheduled! Browser will open automatically.")
pywhatkit.sendwhatmsg(number, msg, hour, minute)