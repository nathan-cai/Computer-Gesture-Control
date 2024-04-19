# Computer-Gesture-Control

Using your webcam perform mouse movements using hand movements and gestures. 

## Description

Using openCV and mediapipe accurately move your mouse using your pointer finger. The tip of your index finger is tracked to move the mouse across the screen. Tap the tip of your thumb and middle finger together to left click. Tap the tip of your thumb and ring finger to right click. Pinch all fingers tips together to exit the program. 

## Getting Started

### Dependencies

Install Python 3.10+ from [Here](https://www.python.org/downloads/)

Then install the following packages using pip

```
pip install mediapipe
pip install pyautogui
pip install opencv-python
```

The required packages are mediapipe for handtracking, pyautogui for mouse controls, and opencv to load images from the webcam.

### Executing program

* Clone this git repository
* Tun main.py using your python interpreter
```
python main.py
```

## Acknowledgments

Inspiration, code snippets, etc.
* [Advanced Computer Vision with Python - Full Course](https://www.youtube.com/watch?v=01sAkU_NvOY)
