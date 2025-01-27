from djitellopy import Tello
import time

# Inizializza il drone
tello = Tello()
tello.connect()
tello.takeoff()

# Distanza di sicurezza dal muro (in cm)
safe_distance = 30

try:
    while True:
        # Ottieni la distanza dal sensore ToF
        distance = tello.get_tof()

        # Se la distanza è minore della distanza di sicurezza, fermati
        if distance < safe_distance:
            print("Muro rilevato! Arresto del movimento.")
            tello.send_rc_control(0, 0, 0, 0)  # Ferma il drone
        else:
            # Altrimenti, continua il movimento (esempio: vai avanti)
            tello.send_rc_control(0, 50, 0, 0)  # Muovi in avanti

        time.sleep(0.1)  # Aggiorna la distanza ogni 0.1 secondi

except KeyboardInterrupt:
    print("Atterraggio...")
    tello.land()