# opening an image on a different window
import cv2

img = cv2.imread('Computer-Vision-with-Python/DATA/00-puppy.jpg')

while True:
    
    cv2.imshow('Puppy', img)

    # if we waiting at least 1ms AND we've pressed the Esc key(27)
    if cv2.waitKey(1) & 0xFF ==  27:
        break
        
cv2.destroyAllWindows()