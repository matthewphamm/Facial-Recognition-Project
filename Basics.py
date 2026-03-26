import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file('ImagesBasic/Elon_Musk.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

faceLocation = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (faceLocation[3], faceLocation[0]), (faceLocation[1], faceLocation[2]), (255, 0, 255), 2)

cv2.imshow('Elon Musk', imgElon)
cv2.waitKey(0)