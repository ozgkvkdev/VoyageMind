from planner import en_uygun_sehri_bul, butce_hesapla
from report import rapor_olustur

print()
print("=" * 50)
print("       VOYAGEMIND'E HOŞ GELDİNİZ")
print("=" * 50)
print("Akıllı Seyahat ve Tatil Planlayıcı")
print("Size en uygun tatil rotasını birlikte bulalım!")
print("=" * 50)

ad = input("Adınızı Giriniz: ")
tatil_butce = int(input("Lütfen Tatil Bütçenizi Giriniz (TL): "))
tatil_gun = int(input("Kaç gün tatil yapmak istiyorsunuz?: "))

print(f"\nMerhaba {ad}")
print("Senin için en uygun tatil rotasını hazırlıyoruz...")
print("-" * 50)

ilgiler = input("İlgi alanlarınızı virgülle ayırarak giriniz: ")
ilgi_listesi = [ilgi.strip() for ilgi in ilgiler.split(",")]

print(f"\nİlgi Alanlarınız: {', '.join(ilgi_listesi)}")

en_iyi_sehir = en_uygun_sehri_bul(ilgi_listesi)

if en_iyi_sehir:

    toplam_maliyet = butce_hesapla(
        en_iyi_sehir["gunluk_ucret"],
        tatil_gun
    )

    rapor_olustur(
        ad,
        en_iyi_sehir,
        tatil_gun,
        tatil_butce,
        toplam_maliyet
    )

else:
    print("\nSize uygun bir şehir bulunamadı.")