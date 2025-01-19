import cv2
import mediapipe as mp
import pyautogui
import os


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils


screenshot_dir = r"D:\Finger Detection\screenshot"


os.makedirs(screenshot_dir, exist_ok=True)


screenshot_taken = False

cap = cv2.VideoCapture(0)

with mp_hands.Hands(static_image_mode=False,
                    max_num_hands=2,
                    min_detection_confidence=0.5,
                    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        finger_counts = []
        total_fingers = 0

        if results.multi_hand_landmarks:
            for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                handedness = hand_handedness.classification[0].label
                fingers_up = 0
                tip_ids = [4, 8, 12, 16, 20]

                
                if handedness == "Right":
                    if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0] - 1].x:
                        fingers_up += 1
                elif handedness == "Left":
                    if hand_landmarks.landmark[tip_ids[0]].x > hand_landmarks.landmark[tip_ids[0] - 1].x:
                        fingers_up += 1

                
                for i in range(1, 5):
                    if hand_landmarks.landmark[tip_ids[i]].y < hand_landmarks.landmark[tip_ids[i] - 2].y:
                        fingers_up += 1

                finger_counts.append(fingers_up)
                total_fingers += fingers_up

                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        
        if total_fingers == 5 and not screenshot_taken:
            
            screenshot_path = os.path.join(screenshot_dir, f"screenshot_{len(os.listdir(screenshot_dir)) + 1}.png")
            pyautogui.screenshot(screenshot_path)  
            cv2.putText(frame, "Screenshot Taken!", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2) 
            screenshot_taken = True  

        print("Screenshot taken!")  
        if total_fingers < 5:
            screenshot_taken = False  

        text = f"Fingers: {', '.join(map(str, finger_counts))} | Total: {total_fingers}"
        cv2.putText(frame, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (35, 25, 50), 2)

        cv2.imshow("Finger Counter", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
