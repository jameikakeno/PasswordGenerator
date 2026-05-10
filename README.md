```markdown
# 🔑 Keneviz - Password Generator Tool

🌟**Bilgi :**  
Keneviz — Güçlü ve rastgele şifreler oluşturmak için geliştirilmiş basit ve etkili bir şifre üretici aracıdır. Harfler, sayılar ve özel karakterler kullanarak istediğiniz uzunlukta şifreler oluşturur.

Bu araç, **Termux**, **Linux**, **Windows** ve tüm ana terminal ortamlarıyla uyumludur.

🐙 **GitHub:** [github.com/jameikakeno/PasswordGenerator](https://github.com/jameikakeno/PasswordGenerator)

---

## ⚡️ Özellikler

* Rastgele güçlü şifre oluşturma (Büyük/Küçük harf + Sayı + Özel Karakter)
* Renkli ve kullanıcı dostu terminal arayüzü
* Oluşturulan şifreleri otomatik olarak `sifreler/` klasörüne kaydetme
* Sonsuz döngü ile sürekli yeni şifre üretebilme
* Klasör yoksa otomatik oluşturma (hata yönetimi)

---

## 🖥 Kurulum

Herhangi bir özel kurulum gerektirmez, sadece Python 3 yüklü olması yeterlidir.

```bash
git clone https://github.com/jameikakeno/PasswordGenerator.git
cd PasswordGenerator
python kenevizpassgen.py
```

---

🗂 Kullanım

1. Programı çalıştırın (python kenevizpassgen.py)
2. İstediğiniz şifre uzunluğunu (rakam olarak) girin
3. Program güçlü bir şifre üretecektir
4. Çıkan şifreyi kullanabilir veya e tuşuna basarak sifreler/ klasörüne kaydedebilirsiniz
5. Yeni şifre oluşturmak için devam edin veya h diyerek çıkış yapın

---

📂 Dosya Yapısı

```
PasswordGenerator/
├── kenevizpassgen.py          (Ana program)
├── sifreler/                  (Kaydedilen şifrelerin klasörü)
└── README.md                  (Bu dosya)
```

---

❓ Sık Sorulan Sorular

S: Şifreler nerede saklanıyor?
C: Eğer kaydetmeyi seçerseniz, programın yanında oluşturulan sifreler/ klasöründe sifre_tarih.txt olarak saklanır.

S: Herhangi bir ek kütüphane kurmam gerekiyor mu?
C: Hayır, program sadece Python standart kütüphanesini kullanır (random, os, time).

---

👨‍💻 Geliştirici

Keneviz
Telegram: @KenevizPremiumTool

---

Keneviz — Güçlü şifreler, güvenli hesaplar! 🔑

```
