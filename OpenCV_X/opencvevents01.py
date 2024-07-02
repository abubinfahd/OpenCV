import pandas as pd
import numpy as np
import cv2

img = np.zeros((512, 512, 3))

def draw(event, x, y, flags, params):
    #print("Event draw")
    #print(event)

    if event == 0:
        print("Mouse moved")
    elif event == 1:
        #print("Left button clicked")
        cv2.circle(img, (x, y), 50, (255, 0, 0), -1)
    elif event == 4:
        print("Left button released")


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()