
import cv2
import numpy as np
import psycopg2
from datetime import datetime


conn = psycopg2.connect(database="yuz_tanima", user="postgres", password="your_password", host="localhost", port="5432")
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

        cursor.execute("SELECT id, ad, soyad, yuz_verisi FROM calisanlar")
        employees = cursor.fetchall()

        for emp_id, ad, soyad, db_face in employees:
            if face_data == db_face:
                now = datetime.now()

                cursor.execute("UPDATE calisanlar SET son_giris = %s WHERE id = %s", (now, emp_id))
                conn.commit()

                print(f"{ad} {soyad} giriş yaptı! ({now})")

                if now.hour >= 9:
                    print(f"{ad} {soyad} geç kaldı!")

        cv2.imshow('Yüz Tanıma', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cam.release()
cv2.destroyAllWindows()
cursor.close()
conn.close()
