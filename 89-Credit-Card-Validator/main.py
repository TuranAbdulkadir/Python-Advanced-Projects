print("--- LUHN ALGORITHM VALIDATOR ---")
card_number = input("Kredi Kartı No Girin: ").replace(" ", "")

def luhn_check(card_num):
    digits = [int(d) for d in str(card_num)]
    # Sondan başla, her ikinci rakamı 2 ile çarp
    checksum = 0
    reverse_digits = digits[::-1]
    
    for i, d in enumerate(reverse_digits):
        if i % 2 == 1:
            doubled = d * 2
            if doubled > 9:
                doubled -= 9
            checksum += doubled
        else:
            checksum += d
            
    return checksum % 10 == 0

if luhn_check(card_number):
    print("✅ GEÇERLİ KART NUMARASI")
    if card_number.startswith("4"): print("Tip: VISA")
    elif card_number.startswith("5"): print("Tip: MasterCard")
else:
    print("❌ GEÇERSİZ KART NUMARASI (Sahte)")