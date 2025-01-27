from djitellopy import Tello
import pygame

# Inizializza Pygame
pygame.init()

# Crea una finestra
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Controllo Tello")

# Crea un oggetto Tello
tello = Tello()
tello.connect()

# Velocità del drone
velocita = 50

# Funzione per visualizzare informazioni sullo schermo
def display_info(screen, tello):
    font = pygame.font.Font(None, 30)
    battery_text = font.render(f"Batteria: {tello.get_battery()}%", True, (255, 255, 255))
    screen.blit(battery_text, (10, 10))

# Ciclo principale
while True:
    # Gestisci gli eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Ottieni lo stato dei tasti
    keys = pygame.key.get_pressed()

    # Muovi il drone con la tastiera
    if keys[pygame.K_t]:
        tello.takeoff()
    if keys[pygame.K_l]:
        tello.land()
    if keys[pygame.K_LEFT]:
        tello.rotate_counter_clockwise(velocita)
    if keys[pygame.K_RIGHT]:
        tello.rotate_clockwise(velocita)
    if keys[pygame.K_UP]:
        tello.move_forward(velocita)
    if keys[pygame.K_DOWN]:
        tello.move_back(velocita)
    if keys[pygame.K_w]:
        tello.move_up(velocita)
    if keys[pygame.K_s]:
        tello.move_down(velocita)
    if keys[pygame.K_a]:
        tello.move_left(velocita)
    if keys[pygame.K_d]:
        tello.move_right(velocita)

    # Muovi il drone con il mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rotation_speed = int((mouse_x - 150) / 150 * velocita)  # -velocita a +velocita
    tello.send_rc_control(0, 0, 0, rotation_speed)
    # Muovi il drone con il mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x != 150:  # Aggiungi questa condizione
        rotation_speed = int((mouse_x - 150) / 150 * velocita)
    else:
        rotation_speed = 0
    tello.send_rc_control(0, 0, 0, rotation_speed)

    # Visualizza le informazioni del drone
    display_info(screen, tello)

    # Aggiorna la finestra
    pygame.display.flip()