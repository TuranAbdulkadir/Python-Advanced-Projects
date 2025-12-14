import re

print("--- SMART CONTRACT AUDITOR ---")

# Örnek Güvensiz Solidity Kodu (Reentrancy Açığı Var)
vulnerable_contract = """
function withdraw() public {
    uint bal = balances[msg.sender];
    require(bal > 0);
    (bool sent, ) = msg.sender.call{value: bal}(""); // Tehlikeli Satır
    require(sent, "Failed to send Ether");
    balances[msg.sender] = 0; // Bakiye güncellemesi işlemden SONRA (HATA!)
}
"""

def audit_code(code):
    print("[*] Solidity Kodu Analiz Ediliyor...")
    issues = []
    
    # Reentrancy Kontrolü: .call() var mı ve bakiye sonra mı sıfırlanıyor?
    if ".call{value:" in code:
        # Basit regex mantığı (Gerçekte AST analizi yapılır)
        call_pos = code.find(".call{value:")
        update_pos = code.find("balances[msg.sender] = 0")
        
        if update_pos > call_pos:
            issues.append("CRITICAL: Reentrancy Vulnerability Detected! (Checks-Effects-Interactions pattern violated)")

    return issues

print("Analyzed Contract:")
print(vulnerable_contract.strip())
print("\n--- REPORT ---")
findings = audit_code(vulnerable_contract)
for f in findings:
    print(f"🚨 {f}")