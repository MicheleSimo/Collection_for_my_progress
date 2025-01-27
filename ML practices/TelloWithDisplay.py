from tello import Tello
import time

drone = Tello()
drone.wait_for_connection(10.0) 

# Visualizza del testo
drone.display_text("Ciao!", color=(255, 0, 0))  # Colore rosso
time.sleep(2)

# Visualizza un numero
drone.display_number(42, color=(0, 255, 0))  # Colore verde
time.sleep(2)

# Visualizza un'immagine predefinita
drone.display_image(drone.IMAGES.HAPPY)
time.sleep(2)

# Crea un'immagine personalizzata (matrice di 8x8)
immagine = [
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
]
drone.display_matrix(immagine, color=(0, 0, 255))  # Colore blu
time.sleep(2)

drone.end()