def rapor_olustur(ad, sehir, tatil_gun, tatil_butce, toplam_maliyet):

    print("\n" + "=" * 50)
    print("           TATİL RAPORU")
    print("=" * 50)

    print(f"Kullanıcı      : {ad}")
    print(f"Şehir          : {sehir['sehir']}")
    print(f"Tatil Süresi   : {tatil_gun} Gün")
    print(f"Tatil Bütçesi  : {tatil_butce} TL")
    print(f"Toplam Maliyet : {toplam_maliyet} TL")

    kalan = tatil_butce - toplam_maliyet

    if kalan >= 0:
        print(f"Kalan Bütçe    : {kalan} TL")
    else:
        print(f"Eksik Tutar    : {abs(kalan)} TL")

    print("=" * 50)