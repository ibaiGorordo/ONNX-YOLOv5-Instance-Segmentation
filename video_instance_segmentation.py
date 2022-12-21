import cv2
from cap_from_youtube import cap_from_youtube

from yoloseg import YOLOSeg

# # Initialize video
# cap = cv2.VideoCapture("input.mp4")

videoUrl = 'https://youtu.be/Atkp8mklOh0'
cap = cap_from_youtube(videoUrl, resolution='720p')
start_time = 5  # skip first {start_time} seconds
cap.set(cv2.CAP_PROP_POS_FRAMES, start_time * cap.get(cv2.CAP_PROP_FPS))

# Initialize YOLOv7 model
model_path = "models/yolov5s-seg.onnx"
yoloseg = YOLOSeg(model_path, conf_thres=0.4, iou_thres=0.3)

cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
frame_countdown = 3
while cap.isOpened():

    # Press key q to stop
    if cv2.waitKey(1) == ord('q'):
        break

    # Read frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Update object localizer
    boxes, scores, class_ids, masks = yoloseg(frame)

    combined_img = yoloseg.draw_masks(frame, mask_alpha=0.4)
    cv2.imshow("Detected Objects", combined_img)

cap.release()