import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
	_,frame=cap.read()
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#hue saturatio n and value
	lower_red=np.array([15,10,0])
	upper_red=np.array([180,255,150])

	mask=cv2.inRange(hsv,lower_red,upper_red)
	res=cv2.bitwise_and(frame,frame,mask=mask)

	kernel=np.ones((5,5),np.uint8)
	erosion=cv2.erode(mask,kernel,iterations=1)
	dilation=cv2.dilate(mask,kernel,iterations=1)

	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	cv2.imshow('frame',frame)
	cv2.imshow('ersion',erosion)
	cv2.imshow('dilation',dilation)
#	cv2.imshow('bilateral',bilateral)

	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
