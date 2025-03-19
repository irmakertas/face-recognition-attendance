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

## 📌Scroll down for English.






# Face Recognition Attendance System

This project is a face recognition-based attendance system that detects employee attendance using OpenCV and PostgreSQL. It consists of two main scripts:

1. **face_recognition.py** - Registers new employees and stores facial data.
2. **attendance.py** - Detects registered employees and logs attendance.

## Requirements

Before running the project, ensure that the following dependencies are installed:

- Python 3.x
- OpenCV
- NumPy
- PostgreSQL
- psycopg2

To install the required Python packages, run the following command:

```bash
pip install opencv-python numpy psycopg2
```

## Database Setup

This project uses a PostgreSQL database. Create a database named `yuz_tanima` and a table `calisanlar` using the following SQL commands:

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

## Usage

### 1. Register Employees
Run the following command to register employees:

```bash
python face_recognition.py
```

- The program captures a face, asks for the employee's first and last name, and saves the facial data in the database.
- Press 'q' to exit.

### 2. Log Attendance
Run the following command to log employee attendance:

```bash
python attendance.py
```

- The program continuously scans for faces.
- If a registered employee is detected, their check-in time is recorded in the database.
- If the check-in time is after 9:00 AM, the system marks the employee as late.
- Press 'q' to exit.

## Notes

- Ensure that your PostgreSQL server is running and that the connection details in the scripts match your database configuration.
- The system currently uses direct byte comparison for face recognition. For a more reliable method, consider using OpenCV’s LBPH, Eigenfaces, or deep learning-based approaches.



