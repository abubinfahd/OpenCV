import cv2
import numpy as np

# building cropping tool
image_path = r"images\apple.jpg"
img = cv2.imread(image_path)

flag = False
ix, iy = -1, -1
fx, fy = -1, -1
def crop(event, x, y, flags, param):
    global ix, iy, fx, fy, flag, img
    
    if event == 1:
        flag = True
        ix, iy = x, y

    # elif event == 0:
    #     if flag == True:
    #         img_copy = img.copy()
    #         cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 0, 255), 1)
    #         cv2.imshow('image', img_copy)

    elif event == 4:

        flag = False
        fx, fy = x, y
        cv2.rectangle(img, (ix, iy), (fx, fy), (0, 0, 255), 1)
        cropped = img[iy:fy, ix:fx]
        cv2.imshow('cropped', cropped)
        cv2.waitKey(0)
    

cv2.namedWindow('image')
cv2.setMouseCallback('image', crop)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
