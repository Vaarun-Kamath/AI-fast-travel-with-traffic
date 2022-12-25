import cv2
import time

#map = cv2.line(map,(0,0),(curr,curr),(0,255,0),10) LINE
#map = cv2.rectangle(map,(100,100),(300,500),(0,0,255),-1) RECT
#map = cv2.circle(map,(100,100),200,(255,0,0),-1) CIRCLE
#map = cv2.putText(map,"Aye GG man",(300,300),cv2.FONT_HERSHEY_PLAIN, 4,(0,0,0),4,cv2.LINE_AA) TEXT

def on_click(event, x, y, p1, p2):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"({x},{y})")

map = cv2.imread('assets/Map2.png',1)
map = cv2.resize(map,(900,900))

height = map.shape[0]
width = map.shape[1]

cv2.imshow('root',map)
cv2.setMouseCallback('root', on_click)

# map = cv2.line(map,(0,0),(width,height),(0,255,0),10)
# map = cv2.rectangle(map,(100,100),(300,500),(0,0,255),-1)
# map = cv2.circle(map,(100,100),200,(255,0,0),-1)

# map = cv2.putText(map,"Aye GG man",(300,300),cv2.FONT_HERSHEY_PLAIN, 4,(0,0,0),4,cv2.LINE_AA)

cv2.imshow('root',map)

cv2.waitKey(0)
cv2.destroyAllWindows()