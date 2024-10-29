#https://www.youtube.com/watch?v=fEdbtmrpFGw

import numpy as np #numpy to work with data
from PIL import ImageGrab #PIL replaces pyautogui
import cv2 #cv2 to work with codec (what is codec?)
from screeninfo import get_monitors #automatic monitor info

#get main monitor info  
for monitor in get_monitors():
    if monitor.x == 0 and monitor.y == 0:
        monitor_x: int = monitor.x
        monitor_y: int = monitor.y
        monitor_width: int = monitor.width
        monitor_height: int = monitor.height

# #real time video recording
cv2.namedWindow("fresh clip cooking", cv2.WINDOW_NORMAL)

#resize real time video to not cover content
cv2.resizeWindow("fresh clip cooking", 480, 270)

#images captured per second
fps = 30

#encoding for video
fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")

#create capture object
captured_video = cv2.VideoWriter("freshly_baked.mp4", fourcc, fps, (monitor_width, monitor_height))

while True:
    #fetch current display and create image
    image = ImageGrab.grab(bbox=(monitor_x,
                          monitor_y,
                          monitor_width, 
                          monitor_height))
    
    #convert image to numpy image
    np_image = np.array(image)

    #convert numpy image to cvt (why t?) image
    cvt_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2RGB)

    #display mini screen
    cv2.imshow('fresh clip cooking', cvt_image)

    #save images to video file
    captured_video.write(cvt_image)

    #exit with escape on the clip window
    key = cv2.waitKey(20)
    if key == 27:
        break

#release video writer// why?
captured_video.release()

#destroy created windows during video recording and showing
cv2.destroyAllWindows()

