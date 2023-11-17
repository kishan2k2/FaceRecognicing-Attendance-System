# import the opencv library 
import cv2 
  
  
# define a video capture object 
vid = cv2.VideoCapture(0) 
harcascade = cv2.CascadeClassifier('static\haarcascade_frontalface_default.xml')
while(True): 
    # if(KeyboardInterrupt):
    #     break
    # Capture the video frame 
    # by frame 
    q = cv2.waitKey(1)
    if q == ord('q'):
        break
    ret, frame = vid.read() 
  
    # Display the resulting frame 
    # cv2.imshow('frame', frame) 
    face = harcascade.detectMultiScale(frame, 1.1, 9)
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+h, y+w), (255, 255, 255), 2)
    cv2.imshow('detectface', frame)
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 