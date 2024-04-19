import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
import pyautogui


def mouse_control(screen_width, screen_height, vid_width, vid_height, lmlist):

    mouse_x = min(max(int(((lmlist[8][1] - 50) / (vid_width-100))
                          * screen_width), 0), screen_width)

    mouse_y = min(max(int(((lmlist[8][2]) / (vid_height-100))
                  * screen_height), 0), screen_height)

    if abs(lmlist[4][1] - lmlist[8][1]) + abs(lmlist[4][2] - lmlist[8][2]) < 15 and \
            abs(lmlist[4][1] - lmlist[12][1]) + abs(lmlist[4][2] - lmlist[12][2]) > 15 and \
            abs(lmlist[4][1] - lmlist[16][1]) + abs(lmlist[4][2] - lmlist[16][2]) > 15 and \
            abs(lmlist[4][1] - lmlist[20][1]) + abs(lmlist[4][2] - lmlist[20][2]) > 15:
        exit()

    pyautogui.moveTo(mouse_x, mouse_y, _pause=False)
    if abs(lmlist[4][1] - lmlist[12][1]) + abs(lmlist[4][2] - lmlist[12][2]) < 15:
        pyautogui.click()
    elif abs(lmlist[4][1] - lmlist[16][1]) + abs(lmlist[4][2] - lmlist[16][2]) < 15:
        pyautogui.rightClick()

    return mouse_x, mouse_y


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = htm.handDetector()
    width = cap.get(3)
    height = cap.get(4)
    pyautogui.FAILSAFE = False
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.makeMPImage(img)

        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            mouse_control(1920, 1080, width, height, lmList)

        ### Uncomment below to show video ###

        # img = detector.findHands(img)
        # cTime = time.time()
        # fps = 1 / (cTime - pTime)
        # pTime = cTime
        # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
        #             (255, 0, 255), 3)
        # cv2.imshow("Image", img)
        # cv2.waitKey(1)


if __name__ == "__main__":
    main()
