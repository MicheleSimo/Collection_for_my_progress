from djitellopy import Tello
import cv2

drone = Tello()
drone.connect()
drone.streamon()

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('Registrazione tello.avi',fourcc,20.0,(960,720))

while True:
    img = drone.get_frame_read().frame
    cv2.imshow("Tello Stream",img)
    out.write(img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
drone.streamoff()
out.release()
cv2.destroyAllWindows()