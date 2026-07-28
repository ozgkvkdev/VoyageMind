# ✈️ VoyageMind - Akıllı Seyahat & Tatil Planlayıcı

VoyageMind, kullanıcıların bütçe, tatil süresi ve kişisel ilgi alanlarına göre en uygun seyahat rotasını çıkaran Python tabanlı bir konsol uygulamasıdır.

## 🚀 Öne Çıkan Özellikler

- **Akıllı Şehir Eşleştirme:** Kullanıcının ilgi alanları ile şehirlerin sunduğu olanakların kesişimini (`set.intersection`) alarak en uygun destinasyonu belirler.
- **Dinamik Bütçe Analizi:** Günlük konaklama, yemek ve aktivite giderlerini hesaplayarak kullanıcı bütçesinin yeterliliğini denetler.
- **Detaylı Seyahat Raporu:** `f-string` formatlamaları ile kullanıcıya özel harcama ve rota özeti sunar.
- **Modüler Yapı:** Veri, mantık ve arayüz katmanları tamamen birbirinden ayrılarak temiz kod ilkelerine uygun geliştirilmiştir.

## 🛠️ Kullanılan Python Konuları & Yapıları

- **Veri Tipleri & Dönüşümleri:** `int`, `float`, `str`, `bool` ve tip dönüşümleri
- **Veri Yapıları:** `dict` (iç içe şehir verileri), `list` ve `set` (ilgi alanları analizi)
- **Kontrol Akışı:** `if / elif / else` ve mantıksal/karşılaştırma operatörleri
- **Döngüler:** `for` ve `while` döngüleri ile menü yönetimi
- **Fonksiyonlar:** Parametreli fonksiyonlar ve `return` değerleri
- **Modüler Programlama:** `import` ve `from ... import ...` kullanımı

## 📁 Proje Dosya Yapısı

```text
VoyageMind/
│
├── main.py           # Kullanıcı etkileşimi ve ana menü döngüsü
├── planner.py        # Bütçe ve algoritma/eşleştirme fonksiyonları
├── data.py           # Şehir verileri, bütçe kalıpları ve set yapıları
├── .gitignore        # Takip edilmeyecek geçici dosyalar
└── README.md         # Proje dokümantasyonu