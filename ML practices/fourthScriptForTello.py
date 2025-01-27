import matplotlib.pyplot as plt
from djitellopy import Tello
import time

# Inizializza il drone
tello = Tello()
tello.connect()


# Inizializza il grafico
plt.ion()  # Modalità interattiva
fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-')
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Altezza (cm)")
ax.set_title("Altezza del drone Tello")

# Lista per memorizzare i dati
tempi = []
altezze = []

# Tempo iniziale
start_time = time.monotonic()

try:
    tello.takeoff()

    # Avanti
    tello.move_forward(50)
    time.sleep(2)

    # Giù
    tello.move_down(50)
    time.sleep(2)

    # Su
    tello.move_up(50)
    time.sleep(2)

    # Indietro
    tello.move_back(50)
    time.sleep(2)

    while True:
        # Leggi l'altezza dal sensore
        altezza = tello.get_height()

        # Aggiungi i dati alle liste
        tempi.append(time.monotonic() - start_time)
        altezze.append(altezza)

        # Aggiorna il grafico
        line.set_data(tempi, altezze)
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        fig.canvas.flush_events()

        time.sleep(0.1)  # Aggiorna ogni 0.1 secondi

except KeyboardInterrupt:
    print("Interruzione...")
    tello.land()

finally:
    tello.land()
    plt.ioff()
    plt.show()