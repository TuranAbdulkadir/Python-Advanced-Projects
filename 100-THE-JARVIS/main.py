import os
import sys
import psutil
import datetime
import pyttsx3
import speech_recognition as sr
from colorama import Fore, init

init(autoreset=True)
engine = pyttsx3.init()

def speak(text):
    print(f"{Fore.CYAN}JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def cpu_status():
    usage = psutil.cpu_percent()
    speak(f"CPU usage is at {usage} percent.")

def check_security():
    speak("Scanning for intruders...")
    # Basit bir kontrol simülasyonu
    speak("System is secure. No active threats found.")

def run_tool(tool_name):
    speak(f"Launching {tool_name} module...")
    # Örnek: Diğer projeleri buradan çağırabilirsin
    # os.system(f"python ../90-Automated-Pentest-Bot/main.py") 
    speak("Module execution completed.")

print(f"{Fore.YELLOW}**********************************")
print(f"{Fore.YELLOW}* PROJECT 100: J.A.R.V.I.S      *")
print(f"{Fore.YELLOW}**********************************")

speak("System online. Waiting for command.")

while True:
    command = input(f"{Fore.GREEN}KOMUT (status/security/hack/exit): ").lower()
    
    if "status" in command:
        cpu_status()
        speak(f"Battery is at {psutil.sensors_battery().percent} percent.")
        
    elif "security" in command:
        check_security()
        
    elif "hack" in command:
        run_tool("Pentest Bot")
        
    elif "exit" in command:
        speak("Shutting down. Goodbye Commander.")
        break
    else:
        speak("Command not recognized.")