#!/usr/bin/python3
import cv2
from imutils.video import VideoStream

try:
    vs = VideoStream(src=0).start()
    while True:
        img = vs.read()
        dims = img.shape[:2]

        cv2.imshow('image',img)
        if cv2.waitKey(1) == ord('q'):
            break
except KeyboardInterrupt:
    pass
cv2.destroyAllWindows()

print("diego has a big booty juicy booty bool")
