import cv2
from djitellopy import Tello
import numpy as np

tello = Tello()
tello.connect()
tello.streamon()

while True:
    frame_read = tello.get_frame_read()
    frame = frame_read.frame

    # Converti l'immagine in HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definisci l'intervallo di colore del Mission Pad (es. rosso)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Crea una maschera per il colore rosso
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Trova i contorni nella maschera
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Se viene trovato un contorno sufficientemente grande, è il Mission Pad
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:  # Soglia per l'area del Mission Pad
            print("Mission Pad rilevato!")
            # ... (codice per controllare il drone) ...

    # Mostra l'immagine elaborata
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

tello.streamoff()
cv2.destroyAllWindows()