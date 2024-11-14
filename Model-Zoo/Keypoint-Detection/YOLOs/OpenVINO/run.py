import onnxruntime as ort

connections = [(4, 2), (2, 0), (3, 1), (1, 0), (0, 6), (6, 8), (8, 10),
         (0, 5), (5, 7), (7, 9), (0, 12), (12, 14), (14, 16), (0, 11), (11, 13), (13, 15)]

onnx_model = YOLOv8Pose(model_path='./yolov8n-pose.onnx', num_of_keypoints = 17)
results = onnx_model.predict([img])
plt.imshow(plot(img.copy(), results[0].copy(), connections)[:, :, ::-1])
plt.show()
