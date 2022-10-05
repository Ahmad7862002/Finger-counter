import cv2
import mediapipe as mp
import time
import math
cap = cv2.VideoCapture()
cap.open(0, cv2.CAP_DSHOW)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
pt = 0
ct = 0
def distance (x1,x2,y1,y2):
    d = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    return d

while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    x8 ,x12 ,x4,x13,x17,x14,x18, y8,y12,y4,y13,y17,y14,y18 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0
    if results.multi_hand_landmarks:
        varu = 0
        for handlm in results.multi_hand_landmarks:
          varu = varu + 1

          for ID, lm in enumerate(handlm.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if ID == 8 :
                  x8 = cx
                  y8 = cy
                if ID == 12:
                  x12 = cx
                  y12 = cy
                if ID == 4 :
                  x4 = cx
                  y4 = cy
                if ID == 13:
                  x13 = cx
                  y13 = cy
                if ID == 14 :
                  x14 = cx
                  y14 = cy
                if ID == 17:
                  x17 = cx
                  y17 = cy
                if ID == 18:
                  x18 = cx
                  y18 = cy
                d1 = distance(x13,x14,y13,y14)
                d2 = distance(x17,x18,y17,y18)
                d3 = distance(x4,x14,y4,y14)
                d = distance(x8,x12,y8,y12)
                if d >= 55 and d <= 155 and d1 <=30 and d2 <= 30 and d3 <= 70:
                  print ("2 fingers")
          mpDraw.draw_landmarks(frame, handlm,mpHands.HAND_CONNECTIONS)

    ct = time.time()
    fps = 1/(ct-pt)
    pt = ct
    cv2.putText(frame,str(int(fps)), (10,65),cv2.FONT_ITALIC,3,(233, 44 ,123),2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break