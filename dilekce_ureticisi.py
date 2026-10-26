#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
En Resmi ve En Gereksiz Dilekçe Üreticisi
Kayyum Onaylı Absürt Bürokratik Motor
"""

import random
import datetime

def uret_dilekce(konu):
    resmi_basliklar = [
        "ACİL VE SON DERECE ÖNEMLİ DİLEKÇE",
        "MAHKEME ONAYI BEKLENEN RESMİ BAŞVURU",
        "KAYYUM TARAFINDAN İNCELENMİŞ CİDDİ TALEP",
        "EVRENSEL ÖNEME HAİZ GEREKSİZ DİLEKÇE"
    ]
    
    giris = [
        "Sayın İlgili Makamlar,",
        "Muhterem Yetkililer,",
        "Yüksek Mahkeme Nezdinde,",
        "Kayyumluk Makamına,"
    ]
    
    govde_parcalari = [
        f"Konu ile ilgili olarak {konu} meselesi tarafımızca titizlikle incelenmiştir.",
        "Bu durumun derhal ve resmi yollarla çözüme kavuşturulması elzemdir.",
        "Aksi takdirde evrenin dengesi bozulabilir (bilimsel değil ama resmi görünüyor).",
        "Talebimin kayıtlara geçirilmesini ve en kısa sürede cevaplandırılmasını arz ederim.",
        "Bu dilekçe tamamen gereksizdir ancak en resmi haliyle yazılmıştır."
    ]
    
    kapanis = [
        "Saygılarımla,",
        "En derin resmi hürmetlerimle,",
        "Kayyum onayıyla,",
        "Mahkeme önünde"
    ]
    
    dilekce = f"""
{random.choice(resmi_basliklar)}
Tarih: {datetime.date.today().strftime('%d.%m.%Y')}

{random.choice(giris)}

"""
    for _ in range(random.randint(3, 6)):
        dilekce += random.choice(govde_parcalari) + "\n\n"
    
    dilekce += f"{random.choice(kapanis)}\n\nİmza: Absürt Vatandaş\n"
    dilekce += "\n# Gizli not: Bürokrasi bazen kendi kendine gülümser."
    
    return dilekce

def main():
    print("=== EN RESMİ VE EN GEREKSİZ DİLEKÇE ÜRETİCİSİ ===")
    print("Kayyum Onaylı | Ciddi Değil Ama Çok Ciddi")
    print()
    konu = input("Lütfen saçma bir konu giriniz (""""örn: kahvem bitti""""): ")
    print("\n" + "="*50)
    print(uret_dilekce(konu))
    print("="*50)
    print("\nDilekçeniz hazır. Mahkemeye vermeden önce iki kez düşünün.")

if __name__ == "__main__":
    main()
