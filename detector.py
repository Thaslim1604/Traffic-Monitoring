from ultralytics import YOLO
import cv2

# Vehicle class IDs in COCO dataset (what YOLOv8 is trained on)
VEHICLE_CLASSES = {
    2: 'Car',
    3: 'Motorcycle',
    5: 'Bus',
    7: 'Truck'
}

model = YOLO('yolov8n.pt')  # downloads automatically on first run

def get_density_level(count):
    if count <= 5:
        return 'Low', '#1D9E75'
    elif count <= 15:
        return 'Medium', '#EF9F27'
    else:
        return 'High', '#E24B4A'

def process_frame(frame):
    results = model(frame, verbose=False)[0]

    counts = {'Car': 0, 'Motorcycle': 0, 'Bus': 0, 'Truck': 0}
    total = 0

    for box in results.boxes:
        cls_id = int(box.cls[0])
        if cls_id in VEHICLE_CLASSES:
            label = VEHICLE_CLASSES[cls_id]
            counts[label] += 1
            total += 1

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 100), 2)
            cv2.putText(frame, f'{label} {conf:.2f}',
                        (x1, y1 - 8),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 200, 100), 1)

    density_label, density_color = get_density_level(total)

    # overlay stats on frame
    overlay_text = [
        f'Total Vehicles: {total}',
        f'Cars: {counts["Car"]}  Trucks: {counts["Truck"]}',
        f'Buses: {counts["Bus"]}  Bikes: {counts["Motorcycle"]}',
        f'Density: {density_label}',
    ]

    y_pos = 30
    for line in overlay_text:
        cv2.putText(frame, line, (15, y_pos),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.65, (255, 255, 255), 2)
        y_pos += 28

    return frame, counts, total, density_label