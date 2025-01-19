 Finger Detection with Screenshot Capture

 Description:
This project utilizes OpenCV, Mediapipe, and PyAutoGUI to implement a real-time finger detection system using a webcam. The program counts the number of fingers detected and automatically takes a screenshot when all five fingers are shown.

 Features:
- Real-time finger detection using Mediapipe.
- Screenshot capture when all five fingers are detected.
- Displays the number of fingers detected on the video feed.
- Works for both left and right hands.

 Installation:
1. Clone the repository:
   bash
   git clone https://github.com/your-username/finger-detection.git
   cd finger-detection
   
2. Install the required Python libraries:
   bash
   pip install opencv-python mediapipe pyautogui
   

3. Create a directory for storing screenshots:
   - Make sure the path D:\Finger Detection\screenshot exists on your machine. You can modify the path in the script if necessary.

 Usage
1. Run the script:
   bash
   python finger_counter.py
   

2. The program will open a webcam window and start detecting fingers in real time.

3. When five fingers are detected, a screenshot will be saved in the specified directory (D:\Finger Detection\screenshot).

4. Press the Esc key to exit the program.

 Project Structure:

Finger Detection/
├── finger_counter.py         # Main Python script for finger detection
├── screenshot/              # Directory to save screenshots
└── README.md               # Project documentation (this file)


 How It Works:
1. Hand Detection:
   - The script uses Mediapipe's hand tracking module to detect hand landmarks in real time.

2. Finger Counting:
   - It calculates the number of fingers raised based on the relative positions of the finger tip and knuckle landmarks.

3. Screenshot Capture:
   - When five fingers are detected, a screenshot is taken using PyAutoGUI and saved to the specified directory.

4. Real-Time Display:
   - The video feed shows the detected hands and displays the number of fingers detected.

 Dependencies
- Python 3.7+
- OpenCV
- Mediapipe
- PyAutoGUI

 Customization
- Change Screenshot Directory:
  Modify the screenshot_dir variable in the script to change the location where screenshots are saved.
  python
  screenshot_dir = r"path_to_your_directory"
  

- Detection Thresholds:
  Adjust the min_detection_confidence and min_tracking_confidence parameters in the Mediapipe Hands class to improve detection performance.

 Example Output
- Screenshots will be saved as screenshot_1.png, screenshot_2.png, etc., in the specified directory.
- The console will display messages such as "Screenshot taken!" when a screenshot is captured.

 License
This project is licensed under the [MIT License](LICENSE).

---

Feel free to improve or modify the project as needed. Contributions are welcome!

