import re

print("--- SMART CONTRACT AUDITOR ---")
# Örnek Solidity kodu (Normalde dosyadan okunur)
contract_code = """
pragma solidity ^0.4.18;
contract Test {
    function withdraw() public {
        msg.sender.call.value(amount)(""); // Reentrancy Tehlikesi
    }
}
"""

vulns = {
    "Reentrancy": r"call\.value",
    "Old Version": r"\^0\.4",
    "Tx.Origin": r"tx\.origin",
    "Self Destruct": r"selfdestruct"
}

print("Analiz Başlıyor...\n")

for vuln, regex in vulns.items():
    if re.search(regex, contract_code):
        print(f"🚨 AÇIK BULUNDU: {vuln}")
        print("  -> Hackerlar bu açığı kullanarak parayı çalabilir.")
    else:
        print(f"✅ Temiz: {vuln}")

print("\nDenetim Tamamlandı.")