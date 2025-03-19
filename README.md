# Yüz Tanıma Yoklama Sistemi

Bu proje, OpenCV ve PostgreSQL kullanarak çalışanların yoklamasını tespit eden bir yüz tanıma tabanlı yoklama sistemidir. İki ana betikten oluşur:

1. **face_recognition.py** - Yeni çalışanları kaydederek yüz verilerini saklar.
2. **attendance.py** - Kayıtlı çalışanları tespit eder ve yoklama kaydını tutar.

## Gereksinimler

Projeyi çalıştırmadan önce aşağıdaki bağımlılıkların kurulu olduğundan emin olun:

- Python 3.x
- OpenCV
- NumPy
- PostgreSQL
- psycopg2

Gerekli Python paketlerini yüklemek için aşağıdaki komutu çalıştırabilirsiniz:

```bash
pip install opencv-python numpy psycopg2
```

## Veritabanı Kurulumu

Bu proje, PostgreSQL veritabanı kullanmaktadır. Aşağıdaki SQL komutlarını kullanarak `yuz_tanima` adlı bir veritabanı ve `calisanlar` adlı bir tablo oluşturun:

```sql
CREATE DATABASE yuz_tanima;

\c yuz_tanima;

CREATE TABLE calisanlar (
    id SERIAL PRIMARY KEY,
    ad VARCHAR(50),
    soyad VARCHAR(50),
    yuz_verisi BYTEA,
    son_giris TIMESTAMP
);
```

## Kullanım

### 1. Çalışanları Kaydetme
Aşağıdaki komutu çalıştırarak çalışanları kaydedin:

```bash
python face_recognition.py
```

- Program, bir yüz yakalar, çalışanın adını ve soyadını ister ve yüz verisini veritabanına kaydeder.
- Çıkmak için 'q' tuşuna basabilirsiniz.

### 2. Yoklama Kaydı
Aşağıdaki komutu çalıştırarak çalışanların yoklamasını kaydedin:

```bash
python attendance.py
```

- Program sürekli olarak yüzleri tarar.
- Kayıtlı bir çalışan tespit edilirse, giriş saati veritabanına kaydedilir.
- Giriş saati 09:00'dan sonra ise sistem çalışanı geç kaldı olarak işaretler.
- Çıkmak için 'q' tuşuna basabilirsiniz.

## Notlar

- PostgreSQL sunucunuzun çalıştığından ve betiklerdeki bağlantı bilgilerinin veritabanı yapılandırmanızla eşleştiğinden emin olun.
- Sistem şu an için yüz tanımayı doğrudan bayt karşılaştırması ile yapmaktadır. Daha güvenilir bir yöntem için OpenCV’nin LBPH, Eigenfaces veya derin öğrenme tabanlı yöntemlerini kullanmayı düşünebilirsiniz.



