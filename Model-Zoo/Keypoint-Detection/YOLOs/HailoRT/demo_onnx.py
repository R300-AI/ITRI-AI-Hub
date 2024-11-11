from utils import YOLOv8Pose, plot
import cv2

connections = [(4, 2), (2, 0), (3, 1), (1, 0), (0, 6), (6, 8), (8, 10),
               (0, 5), (5, 7), (7, 9), (0, 12), (12, 14), (14, 16), (0, 11), (11, 13), (13, 15)]

frame = cv2.resize(cv2.imread('./grace_hopper.jpg'), (640, 640))

onnx_model = YOLOv8Pose(model_path='./yolov8n-pose.onnx', num_of_keypoints = 17)
results = onnx_model.predict([frame])

cv2.imshow('onnx results', plot(frame.copy(), results[0].copy(), connections))
cv2.waitKey(0)