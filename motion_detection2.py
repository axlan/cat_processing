import numpy as np
import cv2
import imutils

cap = cv2.VideoCapture('rtmp://192.168.1.124/bcs/channel0_main.bcs?channel=0&stream=0&user=admin&password=catbus')

# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
# fgbg = cv2.createBackgroundSubtractorGMG()

# while(1):
#     ret, frame = cap.read()

#     fgmask = fgbg.apply(frame)
#     fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

#     cv2.imshow('frame',fgmask)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()


history = 60
varThreshold = 100
detectShadows = True
fgbg = cv2.createBackgroundSubtractorMOG2( history, varThreshold, detectShadows )

while(1):
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=500)

    fgmask = fgbg.apply(frame)
    # bg = fgbg.getBackgroundImage()

    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

