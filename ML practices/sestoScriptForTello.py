from djitellopy import Tello

drone = Tello()
drone.connect()

drone.takeoff()
drone.set_mission_pad_detection_direction(2)
print(drone.get_mission_pad_distance_x)
print(drone.get_mission_pad())

drone.land()