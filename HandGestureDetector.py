# from typing import List


# def classify(l: List[List[int]]):
#     if l[4][2] < l[3][2] + 10 and :
#         return 1
#     else:
#         return 0

# def isThumb(l: List[List[int]]):
#     if l[4][2] < l[3][2] + 10 and abs(l[4][1] - l[1][1]) < 10:
#         if l[4][1]

import HandTrackingModule as h
import mediapipe as mp
import cv2
import time


def main():
    cap = cv2.VideoCapture(0)

    # detector = h.handDetector()

    BaseOptions = mp.tasks.BaseOptions
    GestureRecognizer = mp.tasks.vision.GestureRecognizer
    GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
    VisionRunningMode = mp.tasks.vision.RunningMode

    # Create a gesture recognizer instance with the image mode:
    options = GestureRecognizerOptions(
        base_options=BaseOptions(model_asset_path='gesture_recognizer.task'),
        running_mode=VisionRunningMode.IMAGE)
    with GestureRecognizer.create_from_options(options) as recognizer:
        # The detector is initialized. Use it here.
        # ...
        print("success")

    while True:
        success, img = cap.read()
        recognition_result = recognizer.recognize(img)
        # img = detector.findHands(img)
        # lmList = detector.findPosition(img)
        # if len(lmList) != 0:
        #     print(lmList[4])
        if recognition_result is not None:
            print(recognition_result.gestures[0][0])

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
