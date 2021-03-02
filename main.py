import cv2
import numpy as np
import time

def nothing(x):
    # any operation
    pass

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX

minute1 = -1
minute2 = -1
second1 = -1
second2 = -1

l_h = 76
l_s = 69
l_v = 157
u_h = 180
u_s = 255
u_v = 255

l_h1 = 90
l_s1 = 61
l_v1 = 170
u_h1 = 180
u_s1 = 255
u_v1 = 255

#red mask
low_red = np.array([0, 155, 30])
high_red = np.array([10, 255, 255])
red_mask = cv2.inRange(hsv_frame, low_red, high_red)
low_red = np.array([170, 155, 84])
high_red = np.array([180, 255, 255])
red_mask1 = cv2.inRange(hsv_frame, low_red, high_red)
red_mask = red_mask + red_mask1
red = cv2.bitwise_and(image, image, mask=red_mask)

#blu mask
low_blue = np.array([94, 100, 60])
high_blue = np.array([126, 255, 255])
blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
blue = cv2.bitwise_and(image, image, mask=blue_mask)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_color_1 = np.array([l_h, l_s, l_v])
    upper_color_1 = np.array([u_h, u_s, u_v])

    mask1 = cv2.inRange(hsv, lower_color_1, upper_color_1)
    kernel1 = np.ones((5, 5), np.uint8)
    mask1 = cv2.erode(mask1, kernel1)

    lower_color_2 = np.array([l_h1, l_s1, l_v1])
    upper_color_2 = np.array([u_h1, u_s1, u_v1])

    mask2 = cv2.inRange(hsv, lower_color_2, upper_color_2)
    kernel2 = np.ones((5, 5), np.uint8)
    mask2 = cv2.erode(mask2, kernel2)

    if int(cv2.__version__[0]) > 3:
        # Opencv 4.x.x
        contours1, _ = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours2, _ = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    else:
        # Opencv 3.x.x
        _, contours1, _ = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        _, contours2, _ = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours1:
        area1 = cv2.contourArea(cnt)
        approx1 = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        x = approx1.ravel()[0]
        y = approx1.ravel()[1]

        if area1 > 400:
            cv2.drawContours(frame, [approx1], 0, (0, 0, 0), 5)

            if len(approx1) == 3:
                cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))
                
            elif len(approx1) == 4:
                #if 
                cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))
                minute1 = int(time.strftime('%M'))
                second1 = int(time.strftime('%S'))
                
            elif 10 < len(approx1) < 20:
                cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))
    
    for cnt in contours2:
        area2 = cv2.contourArea(cnt)
        approx2 = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        x = approx2.ravel()[0]
        y = approx2.ravel()[1]

        if area2 > 400:
            cv2.drawContours(frame, [approx2], 0, (0, 0, 0), 5)

            if len(approx2) == 3:
                cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))
                minute2 = int(time.strftime('%M'))
                second2 = int(time.strftime('%S'))
            elif len(approx2) == 4:
                cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))
                
            elif 10 < len(approx2) < 20:
                cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask1", mask1)
    cv2.imshow("Mask2", mask2)

    if minute1 != -1 and second1 != -1 or minute2 !=-1 and second2 != -1:
        cap.release() 
        cv2.destroyAllWindows() 
        break

    if cv2.waitKey(10) & 0xFF == ord('q'): 
        cap.release() 
        cv2.destroyAllWindows() 
        break

if minute1 < minute2:
    print("1 win")
else:
    if minute1 == minute2:
        if second1 < second2:
            print("1 win")
    else:
        print("2 win")
#return

    