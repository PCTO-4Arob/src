import cv2
import numpy as np

lowerBound=np.array([33,80,40])
upperBound=np.array([102,255,255])

cam= cv2.VideoCapture(0)
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

# font=cv2.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX,2,0.5,0,3,1)#

while True:
    ret, img=cam.read()
    img=cv2.resize(img,(340,220))

    #convert BGR to HSV
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # create the Mask
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)
    #morphology
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    maskFinal=maskClose
    conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    cv2.drawContours(img,conts,-1,(255,0,0),3)
    print(conts)
    
    max_dim = [0, 0, 0, 0]
    for element in conts:
        x,y,w,h=cv2.boundingRect(element)
        if (x + w) > max_dim[1]:
            max_dim[0] = x
            max_dim[1] = x + w
            max_dim[2] = y
            max_dim[3] = y + h
            
    cv2.rectangle(img,(max_dim[0],max_dim[2]),(max_dim[1],max_dim[3]),(0,0,255), 2)
    
    #cv2.imshow("maskClose",maskClose)
    #cv2.imshow("maskOpen",maskOpen)
    #cv2.imshow("mask",mask)
    cv2.imshow("cam",img)
    cv2.waitKey(10)