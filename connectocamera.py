# IMPORTANT TIP WHEN WORKING WITH CAMERAS: MAINTAIN ONLY ONE KERNEL RUNNING
# ERRORS APPEAR WHEN MULTIPLE INSTANCES TRY TO ACCESS THE CAMERA SIMULTANEOUSLY
import cv2 
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# video codec optimal in Ubuntu
codec = 'XVID'

framerate = 20

# video saving settings                            
writer = cv2.VideoWriter('mysupervideo.mp4',cv2.VideoWriter_fourcc(*codec), framerate, (width,height))

while True:
    
    ret, frame = cap.read()
    
    writer.write(frame)
    
    # turn the image into grayscale
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release() # stop capturing
writer.release() # release writer
cv2.destroyAllWindows()