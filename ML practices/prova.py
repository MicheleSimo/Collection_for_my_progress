import socket
import time
from tello import Tello

# Indirizzo IP e porta del drone
tello_address = ('192.168.10.2', 8889)  # Sostituisci con l'IP del tuo drone
drone = Tello()

# Crea un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Funzione per inviare comandi
def send_command(command):
    command = command.encode(encoding="utf-8") 
    sent = sock.sendto(command, tello_address)
    print("Inviato: {}".format(command))



# Connessione al drone
send_command("command")
time.sleep(2)

# Visualizza del testo
send_command("displaytext Ciao!")
time.sleep(2)

# Visualizza un numero
send_command("displaynumber 42")
time.sleep(2)

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

# Chiudi la connessione
sock.close()