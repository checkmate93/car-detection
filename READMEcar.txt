🚗 Real-Time Vehicle Detection Using YOLOv8
This Python project uses the YOLOv8 object detection model from Ultralytics to perform real-time vehicle detection on video streams. It can detect cars, trucks, and motorbikes using the pre-trained yolov8n.pt model and displays bounding boxes with confidence scores.

📦 Features
Real-time object detection with YOLOv8

Vehicle classification: Car, Truck, Motorbike

Bounding boxes with labels and confidence scores

Works with video files (can be modified for webcam input)

Uses OpenCV and CVZone for visualization

🛠️ Easy Installation (Beginner Friendly)
Download PyCharm (or use VS Code or any IDE/terminal you prefer).

Create a new Python project.

Install the required packages. You can do this in one of two ways:

Using the terminal (recommended for most users):

bash
Αντιγραφή
Επεξεργασία
pip install ultralytics opencv-python cvzone
Or via PyCharm:

Go to File → Settings → Project: YourProjectName → Python Interpreter

Click the + icon to add packages

Search for and install:

ultralytics

opencv-python

cvzone

Download the main.py file from this repository and place it inside your project folder.

Create a folder named video in the same directory as main.py.

Place your video file inside the video folder. The default code expects a file named cars.mp4:

css
Αντιγραφή
Επεξεργασία
/your-project/
  ├── main.py
  └── video/
      └── cars.mp4
Run the project:

Click the green Run button in PyCharm
OR

Use the terminal:

bash
Αντιγραφή
Επεξεργασία
python main.py
Enjoy real-time vehicle detection!

🧰 Requirements
Install dependencies with:

bash
Αντιγραφή
Επεξεργασία
pip install ultralytics opencv-python cvzone
▶️ Usage
Place your video file in the video/ directory. This project uses video/cars.mp4 by default.

Run the script:

bash
Αντιγραφή
Επεξεργασία
python main.py
Press q to quit the window.

Note: To use a webcam instead of a video file, uncomment the following line and comment out the video line:

python
Αντιγραφή
Επεξεργασία
# cap = cv2.VideoCapture(1)
📂 File Structure
css
Αντιγραφή
Επεξεργασία
├── video/
│   └── cars.mp4        # Input video file
├── main.py             # Detection script
├── README.md
📸 Example Output
Bounding boxes are drawn on detected vehicles with class names and confidence scores:

css
Αντιγραφή
Επεξεργασία
[ Car 0.86 ], [ Truck 0.73 ]
🧠 Model Info
Model: yolov8n.pt (YOLOv8 nano, pretrained on COCO dataset)

Classes used: "car", "truck", "motorbike"

Detection Threshold: confidence > 0.5

✅ License
This project is open-source under the MIT License.