#!/usr/bin/python
import os
import cv2
import numpy as np
from imutils.video import VideoStream

cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
haar_model_dir = os.path.join(cv2_base_dir,'data/haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(haar_model_dir)

try:
    vs = VideoStream(src=0).start()
    while True:
        img = vs.read()
        dims = img.shape[:2]

        img_center = [dims[0]//2, dims[1]//2]
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.2, minNeighbors=5)

        if len(faces) > 0:
            idx_max_face = np.argmax(faces[:,2]*faces[:,3])
            (x,y,w,h) = faces[idx_max_face,:]
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('image',img)
        if cv2.waitKey(1) == ord('q'):
            break

except KeyboardInterrupt:
    pass

cv2.destroyAllWindows()