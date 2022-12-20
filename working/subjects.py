import os
import sys
import cv2
import csv
from cvzone.HandTrackingModule import HandDetector
import cvzone
import time

# from func import FileName

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
detector = HandDetector(detectionCon=0.8)
pTime = 0


class MCQ():
    def __init__(self, data):
        self.question = data[0]
        self.choice1 = data[1]
        self.choice2 = data[2]
        self.choice3 = data[3]
        self.choice4 = data[4]
        self.choice5 = data[5]

        self.userAns = None

    def update(self, cursor, bboxs):

        for x, bbox in enumerate(bboxs):
            x1, y1, x2, y2 = bbox
            if x1 < cursor[0] < x2 and y1 < cursor[1] < y2:
                self.userAns = x + 1
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)


# Import csv file data
pathCSV = "subjects.csv"
with open(pathCSV, newline='\n') as f:
    reader = csv.reader(f)
    dataAll = list(reader)[1:]

# Create Object for each MCQ
mcqList = []
for q in dataAll:
    mcqList.append(MCQ(q))

print("Total MCQ Objects Created:", len(mcqList))

qNo = 0
qTotal = len(dataAll)


def Matem():
    exec(open('Matem.py').read())


def Geo():
    exec(open('Geo.py').read())


def Pisic():
    exec(open('Pisic.py').read())


def Geometry():
    exec(open('Geometry.py').read())


def MainFunc():
    exec(open('func.py').read())


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if qNo < qTotal:
        mcq = mcqList[qNo]

        img, bbox = cvzone.putTextRect(img, mcq.question, [100, 100], 2, 2, offset=50, border=5)
        img, bbox1 = cvzone.putTextRect(img, mcq.choice1, [100, 250], 2, 2, offset=50, border=5)
        img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [400, 250], 2, 2, offset=50, border=5)
        img, bbox3 = cvzone.putTextRect(img, mcq.choice3, [100, 400], 2, 2, offset=50, border=5)
        img, bbox4 = cvzone.putTextRect(img, mcq.choice4, [400, 400], 2, 2, offset=50, border=5)
        img, bbox5 = cvzone.putTextRect(img, mcq.choice5, [1100, 100], 2, 2, offset=50, border=5)

        name = MainFunc()
        #
        if hands:
            lmList = hands[0]['lmList']
            cursor = lmList[8]
            length, info, img = detector.findDistance(lmList[8][:2], lmList[12][:2], img)
            # print(length)

            if length < 35:
                mcq.update(cursor, [bbox1])
                if mcq.userAns is not None:
                    time.sleep(0.3)
                    text = Matem()
                    # MainFunc()

            if length < 35:
                mcq.update(cursor, [bbox2])
                if mcq.userAns is not None:
                    time.sleep(0.3)
                    Geo()
            if length < 35:
                mcq.update(cursor, [bbox4])
                if mcq.userAns is not None:
                    time.sleep(0.3)
                    Pisic()

            if length < 35:
                mcq.update(cursor, [bbox3])
                if mcq.userAns is not None:
                    time.sleep(0.3)
                    Geometry()
            if length < 35:
                mcq.update(cursor, [bbox5])
                if mcq.userAns is not None:
                    time.sleep(0.3)
                    sys.exit()
            if length < 35:
                mcq.update(cursor, [bbox2])
                if mcq.userAns is not None:
                    time.sleep(0.3)
                    Geometry()

    else:
        score = 0

    cv2.imshow("Img", img)
    if cv2.waitKey(1) == ord('q'):
        sys.exit()
