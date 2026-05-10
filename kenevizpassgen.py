
"""
Developer: Keneviz
Telegram: @KenevizPremiumTool
"""

import random
import os
import sys
import time

KIRMIZI = '\033[91m'
YESIL = '\033[92m'
SARI = '\033[93m'
MAVI = '\033[94m'
MOR = '\033[95m'
CAM = '\033[96m'
BEYAZ = '\033[97m'
KALIN = '\033[1m'
RENK_SIFIRLA = '\033[0m'

def keneviz_banner():

    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""
{YESIL}{KALIN}            _  __      {KIRMIZI}Passwørd Generator Tool{YESIL}      _         
{YESIL}           | |/ /   ___   _ __     ___  __   __ (_)  ____  
{YESIL}           | ' /   / _ \\ | '_ \\   / _ \\ \\ \\ / / | | |_  /  
{YESIL}           | . \\  |  __/ | | | | |  __/  \\ V /  | |  / /   
{YESIL}           |_|\\_\\  \\___| |_| |_|  \\___|   \\_/   |_| /___|  
{CAM}                            Dev : Keneviz
{YESIL}═══════════════════════════════════════════════════════════════{RENK_SIFIRLA}
    """)

def keneviz_password_generator():
    try:
        while True:
            keneviz_banner()
            
            print(f"{SARI}{KALIN}              <===[[ Keneviz Tarafından Kodlandı ]]===>{RENK_SIFIRLA}")
            print(" ")
            print(f"{CAM}{KALIN}        <---( Telegram: @KenevizPremiumTool )--->{RENK_SIFIRLA}")
            print(" ")
            
            try:
                uzunluk = int(input(f"{CAM}{KALIN}Şifre Uzunluğunu Girin (Rakam) : {RENK_SIFIRLA}"))
                if uzunluk <= 0:
                    print(f"\n{KIRMIZI}Uzunluk 0'dan büyük olmalı!{RENK_SIFIRLA}")
                    time.sleep(1)
                    continue
                if uzunluk > 100:
                    print(f"\n{SARI}Uyarı: Çok uzun şifre oluşturuluyor...{RENK_SIFIRLA}")
            except ValueError:
                print(f"\n{KIRMIZI}Lütfen geçerli bir sayı girin!{RENK_SIFIRLA}")
                time.sleep(1)
                continue
            
            print(" ")
            print(f"{SARI}{KALIN}-----> Oluşturulan Şifre <-----{RENK_SIFIRLA}")
            print(" ")
            karakterler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%&*^!?"
            
            sifre = ""
            for i in range(uzunluk):
                sifre += random.choice(karakterler)
            
            print(f"{YESIL}{KALIN} {sifre}{RENK_SIFIRLA}")
            print(" ")
            print(f"{SARI}{KALIN}-----> Şifreni Al <-----{RENK_SIFIRLA}")
            print(" ")
            
            kaydet = input(f"{CAM}Şifreyi dosyaya kaydetmek ister misin? (e/h): {RENK_SIFIRLA}").lower()
            if kaydet == 'e' or kaydet == 'evet':
                if not os.path.exists("sifreler"):
                    os.mkdir("sifreler")
                zaman = time.strftime("%Y-%m-%d_%H-%M-%S")
                dosya_adi = f"sifreler/Keneviz Password Generator {uzunluk} Haneli.txt"
                with open(dosya_adi, 'w', encoding='utf-8') as dosya:
                    dosya.write(f"Keneviz Password Generator\n")
                    dosya.write(f"Tarih: {time.ctime()}\n")
                    dosya.write(f"Uzunluk: {uzunluk}\n")
                    dosya.write(f"Şifre: {sifre}\n")
                    dosya.write(f"Telegram: @KenevizPremiumTool\n")
                print(f"\n{YESIL}[✓] Şifre kaydedildi: {dosya_adi}{RENK_SIFIRLA}")
                time.sleep(1.5)
            print(" ")
            devam = input(f"{CAM}Yeni şifre oluşturmak ister misin? (e/h): {RENK_SIFIRLA}").lower()
            if devam != 'e' and devam != 'evet':
                print(f"\n{YESIL}Keneviz Password Generator Kullandığınız İçin Teşekkürler!{RENK_SIFIRLA}")
                print(f"{CAM}Telegram: @KenevizPremiumTool{RENK_SIFIRLA}")
                time.sleep(2)
                break
            
    except KeyboardInterrupt:
        print(f"\n\n{KIRMIZI}Çıkış yapılıyor...{RENK_SIFIRLA}")
        sys.exit()

if __name__ == "__main__":
    keneviz_password_generator()
