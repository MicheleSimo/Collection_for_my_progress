import pygame
import Box2D
from Box2D.b2 import world, polygonShape, staticBody, dynamicBody, revoluteJointDef

# Inizializzazione di Pygame
pygame.init()

# Dimensioni della finestra
LARGHEZZA, ALTEZZA = 800, 600
finestra = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Robot con Terreno e Rotazione di Arti")

# Colori
BIANCO = (255, 255, 255)
ROSSO = (255, 0, 0)
BLU = (0, 0, 255)
VERDE = (0, 255, 0)
NERO = (0, 0, 0)

# Configurazione Box2D
PPM = 20.0  # Pixel per metro
TIME_STEP = 1.0 / 60  # Tempo tra aggiornamenti
VEL_IT = 6  # Iterazioni di velocità
POS_IT = 2  # Iterazioni di posizione

# Creazione del mondo fisico
mondo = world(gravity=(0, -10), doSleep=True)

# Funzione per convertire le coordinate Box2D in coordinate Pygame
def box2d_to_pygame(pos):
    return int(pos[0] * PPM), ALTEZZA - int(pos[1] * PPM)

# Funzione per creare un rettangolo nel mondo Box2D
def crea_rettangolo(mondo, posizione, dimensioni, dinamico=True):
    corpo = mondo.CreateDynamicBody(position=posizione) if dinamico else mondo.CreateStaticBody(position=posizione)
    corpo.CreatePolygonFixture(box=dimensioni, density=1.0, friction=0.3)
    return corpo

# Creazione del terreno
terreno = crea_rettangolo(mondo, (20, 2), (20, 1), dinamico=False)

# Creazione del robot
# Petto
petto = crea_rettangolo(mondo, (10, 15), (1, 2))
# Braccia
braccio_sx = crea_rettangolo(mondo, (8.5, 15), (0.5, 2))
braccio_dx = crea_rettangolo(mondo, (11.5, 15), (0.5, 2))
# Gambe
gamba_sx = crea_rettangolo(mondo, (9, 12), (0.5, 2))
gamba_dx = crea_rettangolo(mondo, (11, 12), (0.5, 2))

# Giunti
giunto_braccio_sx = mondo.CreateRevoluteJoint(
    bodyA=petto, bodyB=braccio_sx,
    anchor=(8.5, 15),
    lowerAngle=-1.0, upperAngle=1.0,  # Rotazione limitata
    enableLimit=True
)

giunto_braccio_dx = mondo.CreateRevoluteJoint(
    bodyA=petto, bodyB=braccio_dx,
    anchor=(11.5, 15),
    lowerAngle=-1.0, upperAngle=1.0,
    enableLimit=True
)

giunto_gamba_sx = mondo.CreateRevoluteJoint(
    bodyA=petto, bodyB=gamba_sx,
    anchor=(9, 12),
    lowerAngle=-1.0, upperAngle=1.0,
    enableLimit=True
)

giunto_gamba_dx = mondo.CreateRevoluteJoint(
    bodyA=petto, bodyB=gamba_dx,
    anchor=(11, 12),
    lowerAngle=-1.0, upperAngle=1.0,
    enableLimit=True
)

# Loop principale
esegui = True
clock = pygame.time.Clock()

while esegui:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            esegui = False

    # Input da tastiera per controllare i giunti
    tasti = pygame.key.get_pressed()

    # Controlli per i giunti
    if tasti[pygame.K_q]:
        giunto_braccio_sx.motorSpeed = 2.0
        giunto_braccio_sx.maxMotorTorque = 10.0
        giunto_braccio_sx.enableMotor = True
    elif tasti[pygame.K_a]:
        giunto_braccio_sx.motorSpeed = -2.0
        giunto_braccio_sx.maxMotorTorque = 10.0
        giunto_braccio_sx.enableMotor = True
    else:
        giunto_braccio_sx.enableMotor = False

    if tasti[pygame.K_e]:
        giunto_braccio_dx.motorSpeed = 2.0
        giunto_braccio_dx.maxMotorTorque = 10.0
        giunto_braccio_dx.enableMotor = True
    elif tasti[pygame.K_d]:
        giunto_braccio_dx.motorSpeed = -2.0
        giunto_braccio_dx.maxMotorTorque = 10.0
        giunto_braccio_dx.enableMotor = True
    else:
        giunto_braccio_dx.enableMotor = False

    if tasti[pygame.K_z]:
        giunto_gamba_sx.motorSpeed = 2.0
        giunto_gamba_sx.maxMotorTorque = 10.0
        giunto_gamba_sx.enableMotor = True
    elif tasti[pygame.K_x]:
        giunto_gamba_sx.motorSpeed = -2.0
        giunto_gamba_sx.maxMotorTorque = 10.0
        giunto_gamba_sx.enableMotor = True
    else:
        giunto_gamba_sx.enableMotor = False

    if tasti[pygame.K_c]:
        giunto_gamba_dx.motorSpeed = 2.0
        giunto_gamba_dx.maxMotorTorque = 10.0
        giunto_gamba_dx.enableMotor = True
    elif tasti[pygame.K_v]:
        giunto_gamba_dx.motorSpeed = -2.0
        giunto_gamba_dx.maxMotorTorque = 10.0
        giunto_gamba_dx.enableMotor = True
    else:
        giunto_gamba_dx.enableMotor = False

    # Aggiornamento del mondo fisico
    mondo.Step(TIME_STEP, VEL_IT, POS_IT)

    # Disegno
    finestra.fill(BIANCO)

    for corpo in [petto, braccio_sx, braccio_dx, gamba_sx, gamba_dx, terreno]:
        for fixture in corpo.fixtures:
            forma = fixture.shape
            punti = [corpo.transform * v * PPM for v in forma.vertices]
            punti = [(p[0], ALTEZZA - p[1]) for p in punti]
            pygame.draw.polygon(finestra, BLU, punti)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
