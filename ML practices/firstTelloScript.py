from djitellopy import Tello

# Sostituisci "192.168.10.1" con l'indirizzo IP del tuo drone Tello
drone = Tello() 
drone.connect()
drone.takeoff()
#drone.sleep(2)
#drone.move_forward(50)
#drone.sleep(2)
drone.rotate_clockwise(90)
#drone.sleep(1)
drone.move_forward(100)
drone.rotate_counter_clockwise(180)
drone.move_forward(100)
#drone.rotate_counter_clockwise(90)
#drone.sleep(2)

#drone.move_back(90)
#drone.sleep(2)

drone.land()