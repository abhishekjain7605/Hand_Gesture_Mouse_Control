import cv2
import mediapipe as mp
import pyautogui
import time
import numpy as np

# Initialize
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils
screen_w, screen_h = pyautogui.size()

# Smoothing variables
prev_x, prev_y = 0, 0
smoothening = 7

# Cooldown mechanism to prevent gesture spamming
gesture_cooldown = 1.0  # seconds
last_gesture_time = time.time()

def get_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def get_coords(landmark, w, h):
    return int(landmark.x * w), int(landmark.y * h)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    h, w, _ = frame.shape

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm = hand_landmarks.landmark

            # Get coordinates
            ix, iy = get_coords(lm[mp_hands.HandLandmark.INDEX_FINGER_TIP], w, h)
            mx, my = get_coords(lm[mp_hands.HandLandmark.MIDDLE_FINGER_TIP], w, h)
            rx, ry = get_coords(lm[mp_hands.HandLandmark.RING_FINGER_TIP], w, h)
            tx, ty = get_coords(lm[mp_hands.HandLandmark.THUMB_TIP], w, h)
            imx, imy = get_coords(lm[mp_hands.HandLandmark.INDEX_FINGER_MCP], w, h)

            # Draw points
            for id in [ix, iy, mx, my, rx, ry, tx, ty]:
                cv2.circle(frame, (ix, iy), 7, (0, 255, 0), -1)

            # Move mouse smoothly
            screen_x = np.interp(imx, (0, w), (0, screen_w))
            screen_y = np.interp(imy, (0, h), (0, screen_h))
            curr_x = prev_x + (screen_x - prev_x) / smoothening
            curr_y = prev_y + (screen_y - prev_y) / smoothening
            pyautogui.moveTo(curr_x, curr_y)
            prev_x, prev_y = curr_x, curr_y

            # Gesture actions
            now = time.time()
            if now - last_gesture_time > gesture_cooldown:
                if get_distance((ix, iy), (tx, ty)) < 40:
                    pyautogui.click()
                    last_gesture_time = now
                elif get_distance((mx, my), (tx, ty)) < 40:
                    pyautogui.doubleClick()
                    last_gesture_time = now
                elif get_distance((rx, ry), (tx, ty)) < 40:
                    pyautogui.rightClick()
                    last_gesture_time = now
                elif get_distance((ix, iy), (mx, my)) < 40:
                    pyautogui.scroll(5 if imy < my else -5)
                    last_gesture_time = now

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Virtual Mouse", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
