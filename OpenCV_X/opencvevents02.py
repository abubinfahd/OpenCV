import numpy as np
import cv2

img = np.zeros((512, 512, 3))

flag = False
ix = -1
iy = -1
def draw(event, x, y, flags, params):
    global flag, ix, iy


    if event == 1:
        flag = True
        ix, iy = x, y
    
    elif event == 0:

        if flags == True:
            cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)

    elif event == 4:
        flag = False 
        cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()