from data import sehirler


def sehirleri_listele () :
    print("\n Mevcut Şehirler\n")

    for sehir in sehirler:
        print(f"Şehir {sehir['sehir']}")
        print(f"Günlük Ücret {sehir['gunluk_ucret']} TL")

        print(f"Aktiviteler:")
        for aktivite in sehir['aktiviteler']:
            print(f"- {aktivite}")
            print("-"*35)


def en_uygun_sehri_bul(ilgi_listesi):

    en_yuksek_eslesme = 0
    en_iyi_sehir = None

    for sehir in sehirler:

        eslesen_sayi = 0

        for aktivite in sehir["aktiviteler"]:
            if aktivite in ilgi_listesi:
                eslesen_sayi += 1

        if eslesen_sayi > en_yuksek_eslesme:
            en_yuksek_eslesme = eslesen_sayi
            en_iyi_sehir = sehir

    return en_iyi_sehir


def butce_hesapla(gunluk_ucret,tatil_gun):
    toplam_maliyet=gunluk_ucret*tatil_gun
    return toplam_maliyet



    
