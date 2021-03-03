import numpy as np
import argparse
import cv2

webcam = cv2.VideoCapture(0) 

while True:

    _, image = webcam.read()
    hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #red    
    low_red = np.array([0, 155, 30])
    high_red = np.array([10, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    
    low_red = np.array([170, 155, 84])
    high_red = np.array([180, 255, 255])
    red_mask1 = cv2.inRange(hsv_frame, low_red, high_red)
    
    red_mask = red_mask + red_mask1

    red = cv2.bitwise_and(image, image, mask=red_mask)

    #blue
    low_blue = np.array([94, 100, 60])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(image, image, mask=blue_mask)

    #green
    low_green = np.array([25, 72, 80])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(image, image, mask=green_mask)

    final = green_mask + blue_mask + red_mask

    #except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(image, image, mask=mask)


    #cv2.imshow("Frame", image)
    cv2.imshow("hsv", hsv_frame)
    #cv2.imshow("Red", red)
    #cv2.imshow("Blue", blue)
    #cv2.imshow("Green", green)
    cv2.imshow("Result", final)

    if cv2.waitKey(10) & 0xFF == ord('q'): 
        cap.release() 
        cv2.destroyAllWindows() 
        break