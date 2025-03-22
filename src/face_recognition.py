import cv2
import numpy as np
import psycopg2

conn = psycopg2.connect(database="yuz_tanima", user="your_username", password="your_password", host="localhost", port="5432")
cursor = conn.cursor()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (100, 100))
        face_data = np.array(face).tobytes()

        ad = input("Çalışanın adı: ")
        soyad = input("Çalışanın soyadı: ")

        cursor.execute("INSERT INTO calisanlar (ad, soyad, yuz_verisi) VALUES (%s, %s, %s)", (ad, soyad, face_data))
        conn.commit()

        print(f'{ad} {soyad} başarıyla kaydedildi')

    cv2.imshow('Yüz Kaydetme', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
cursor.close()
conn.close()
