from djitellopy import Tello
import time

drone = Tello()
drone.connect()
#drone.wait_for_connection(60.0)

# Abilita il rilevamento dei Mission Pad
drone.enable_mission_pads()

# Decollo
drone.takeoff()

# Vola verso il Mission Pad con ID 1
drone.go_to_mission_pad(1, x=0, y=0, z=50, speed=30)
time.sleep(3)  # Attendi che il drone raggiunga il Mission Pad

# Esegui un'azione quando il drone rileva il Mission Pad
if drone.detect_mission_pad():
    print("Mission Pad 1 rilevato!")
    drone.rotate_clockwise(90)  # Esempio di azione

# Atterra sul Mission Pad con ID 2
drone.go_to_mission_pad(2, x=0, y=0, z=0, speed=30)
drone.land()

drone.end()