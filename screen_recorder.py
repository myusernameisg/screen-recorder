#https://www.geeksforgeeks.org/create-a-screen-recorder-using-python/

import numpy as np #numpy to work with data
import pyautogui #pyautogui to work with?
import cv2 #cv2 to work with codec (what is codec?)

#video parameters#
#resolution of video
resolution_normal = (1920, 1080)

#video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

#output file name
filename = "fresh_clip.avi"

#frames per second of video recording
fps = 30.0 #save data :c
#video parameters#

#video writer object to take in video recording parameters
out = cv2.VideoWriter(filename, codec, fps, resolution)

#real time video parameters
#real time video recording
cv2.namedWindow("fresh clip cooking", cv2.WINDOW_NORMAL)

#resize real time video to not cover content
cv2.resizeWindow("fresh clip cooking", 480, 270)

#video loop
while True:
    #Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    #Convert screenshot to numpy array format
    frame = np.array(img)

    #convert from BGR to RBG (what is BGR??)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #write reformatted image to output file
    out.write(frame)

    #display mini screen
    cv2.imshow('fresh clip cooking', frame)

    #exit recording with "q"
    if cv2.waitKey(1) ==ord('q'):
        break

#release video writer// why?
out.release

#destroy created windows during video recording and showing
cv2.destroyAllWindows()
