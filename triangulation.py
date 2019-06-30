import cv2
import math

def sign(wsize,xmid):
	if xmid<wsize//2:
		return -1
	return 1

def intersection(x1,y1,m1,x2,y2,m2):
	c1 = y1-m1*x1
	c2 = y2-m2*x2
	x = (c2-c1)/(m1-m2)
	y = m1*x+c1
	return int(x),int(y)



img = cv2.imread("floor.png",1)

l = 7
b = 6
unit = 100
l = l*unit
b = b*unit

length = 800
offset = 100

theta = 60
theta = math.radians(theta)
pi = math.radians(90)

wsize = 640
cdist = wsize/(2*math.tan(theta/2))

xmid1 = 360
xmid2 = 160
angle1 = math.atan(abs(xmid1-wsize/2)/cdist)
angle2 = math.atan(abs(xmid2-wsize/2)/cdist)



cv2.rectangle(img,(offset,offset),(l+offset,b+offset),(255,255,255),2)


cv2.line(img,(offset+l//2,offset),(offset+l//2 + int(length*math.sin(theta/2)),offset+ int(length*math.cos(theta/2))),(255,0,255),1)
cv2.line(img,(offset+l//2,offset),(offset+l//2 - int(length*math.sin(theta/2)),offset+ int(length*math.cos((theta/2)))),(255,0,255),1)

cv2.line(img,(offset,offset+b//2),(offset + int(length*math.sin(pi-theta/2)),offset+ b//2+int(length*math.cos((pi-theta/2)))),(0,255,255),1)
cv2.line(img,(offset,offset+b//2),(offset + int(length*math.sin(pi-theta/2)),offset+ b//2-int(length*math.cos((pi-theta/2)))),(0,255,255),1)

cv2.line(img,(offset+l//2,offset),(offset+l//2  +sign(wsize,xmid1)*int(length*math.sin(angle1)),offset+ int(length*math.cos(angle1))),(0,0,255),2)
cv2.line(img,(offset,offset+b//2),(offset + int(length*math.sin(pi-angle2)),offset+ b//2+sign(wsize,xmid2)*int(length*math.cos((pi-angle2)))),(0,255,0),2)


cv2.circle(img,(offset+l//2,offset), 15, (255,255,255), -1)
cv2.circle(img,(offset,offset+b//2), 15, (255,255,255), -1)

m1 = math.tan(pi-sign(wsize,xmid1)*angle1)
m2 = math.tan(1*sign(wsize,xmid2)*angle2)

x,y = intersection(offset+l//2,offset, m1,offset,offset+b//2,m2  )
cv2.circle(img,(x,y), 10, (255,255,255), 2)
cv2.imshow('floor',img)
cv2.waitKey(0)
cv2.destroyAllWindows()