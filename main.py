import cv2
import time
from ultralytics import YOLO

# ===========================
# Load YOLO Model
# ===========================
model = YOLO("yolov8n.pt")  # Change to yolov8s.pt for better accuracy

# ===========================
# Webcam
# ===========================
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

# ===========================
# FPS Calculation
# ===========================
prev_time = time.time()

# ===========================
# Main Loop
# ===========================
while True:

    ret, frame = cap.read()

    if not ret:
        break

    # ---------------------------
    # FPS
    # ---------------------------
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    # ---------------------------
    # Object Statistics
    # ---------------------------
    object_counts = {}

    # ---------------------------
    # Run YOLO
    # ---------------------------
    results = model(frame, verbose=False)

    for result in results:

        boxes = result.boxes

        for box in boxes:

            # ---------------------------
            # Bounding Box
            # ---------------------------
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # ---------------------------
            # Class
            # ---------------------------
            cls = int(box.cls[0])
            class_name = model.names[cls]

            # ---------------------------
            # Confidence
            # ---------------------------
            confidence = float(box.conf[0])
            confidence_percent = int(confidence * 100)

            # Ignore very weak detections
            if confidence < 0.30:
                continue

            # ---------------------------
            # Count Objects
            # ---------------------------
            object_counts[class_name] = object_counts.get(class_name, 0) + 1

            # ---------------------------
            # Color Based on Confidence
            # ---------------------------
            if confidence > 0.80:
                color = (0, 255, 0)      # Green
            elif confidence > 0.50:
                color = (0, 255, 255)    # Yellow
            else:
                color = (0, 0, 255)      # Red

            # ---------------------------
            # Draw Bounding Box
            # ---------------------------
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                color,
                2
            )

            # ---------------------------
            # Label
            # ---------------------------
            label = f"{class_name} {confidence_percent}%"

            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

            # ---------------------------
            # Confidence Bar
            # ---------------------------
            bar_width = 100
            bar_height = 8

            bar_x = x1
            bar_y = y2 + 10

            # Background
            cv2.rectangle(
                frame,
                (bar_x, bar_y),
                (bar_x + bar_width, bar_y + bar_height),
                (70, 70, 70),
                -1
            )

            # Filled
            filled_width = int(bar_width * confidence)

            cv2.rectangle(
                frame,
                (bar_x, bar_y),
                (bar_x + filled_width, bar_y + bar_height),
                color,
                -1
            )

    # ===========================
    # Dashboard Panel
    # ===========================

    panel_width = 320

    cv2.rectangle(
        frame,
        (0, 0),
        (panel_width, frame.shape[0]),
        (30, 30, 30),
        -1
    )

    cv2.putText(
        frame,
        "SMART AI CCTV",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"FPS : {int(fps)}",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    total_objects = sum(object_counts.values())

    cv2.putText(
        frame,
        f"Objects : {total_objects}",
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "Status : ONLINE",
        (20, 130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.line(
        frame,
        (20, 150),
        (280, 150),
        (100, 100, 100),
        2
    )

    cv2.putText(
        frame,
        "Detected Objects",
        (20, 175),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2
    )

    y = 210

    # Sort by count (highest first)
    sorted_objects = sorted(
        object_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for name, count in sorted_objects:

        cv2.putText(
            frame,
            f"{name}: {count}",
            (20, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        y += 25

    # ===========================
    # Show Window
    # ===========================
    cv2.imshow("Smart AI CCTV", frame)

    # ESC to Quit
    if cv2.waitKey(1) & 0xFF == 27:
        break

# ===========================
# Cleanup
# ===========================
cap.release()
cv2.destroyAllWindows()