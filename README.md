# MLE-Tahmin

## Aktüerya için MLE Parametre Tahmin Programı

**(Gamma, Pareto, Lomax)**

---

### 👤 Geliştirici

* **Ad–Soyad:** Melih Karagülmez
* **Bölüm:** Aktüerya Bilimleri

---

## 📊 Aktüeryal Dağılım Tahmin Sistemi

Bu proje, sigorta ve finans sektöründe sıklıkla karşılaşılan **hasar / tutar verilerini** analiz etmek amacıyla geliştirilmiş bir **Python tabanlı MLE (Maximum Likelihood Estimation)** aracıdır.

Veri setinize en uygun:

* **Gamma**
* **Pareto (Tip I)**
* **Lomax (Pareto Tip II)**

dağılımlarının parametrelerini **otomatik olarak** hesaplar.

---

## 🚀 Özellikler

### 🔹 Çoklu Dağılım Desteği

* **📘 Gamma:** Genel hasar tutarları için
* **📗 Pareto (Tip I):** Büyük hasarlar, kuyruk riski ve reasürans analizleri
* **📙 Lomax (Pareto Tip II):** Ağır kuyruklu verilerde esnek modelleme

### 🔹 Akıllı Veri Temizliği

* Negatif ve **0 veya altı** değerleri otomatik tespit eder
* Analiz dışı bırakır
* Kullanıcıyı bilgilendirir

### 🔹 Türkçe Format Desteği

* Excel kaynaklı CSV dosyalarındaki
  **virgüllü ondalık sayıları (örn: 1,25)** sorunsuz okur

### 🔹 İnteraktif Kullanım

* Dosya adı ve dağılım türü
* **Komut satırı üzerinden kullanıcıdan alınır**

---

## 🛠️ Kurulum

Gerekli kütüphaneleri yüklemek için terminalde:

pip install -r requirements.txt

komutunu çalıştırmanız yeterlidir.

---

## 📌 Not

Bu proje **aktüeryal modelleme**, **risk analizi** ve **istatistiksel dağılım tahmini** dersleri için uygundur ve akademik amaçla geliştirilmiştir.
