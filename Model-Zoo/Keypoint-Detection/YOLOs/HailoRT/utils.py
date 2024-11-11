import numpy as np
import cv2
import onnxruntime as ort

class YOLOv8Pose():
    def __init__(self, model_path, nc = 1, num_of_keypoints = 17):
        self.session = ort.InferenceSession(model_path)
        self.input_details  = [i for i in self.session.get_inputs()]
        self.output_details = [i.name for i in self.session.get_outputs()]
        self.X_axis = [0, 2] + [5 + i * 3 for i in range(num_of_keypoints)]
        self.y_axis = [1, 3] + [6 + i * 3 for i in range(num_of_keypoints)]
        self.nc = nc

    def predict(self, frames, conf=0.25, iou=0.7, agnostic=False, max_det=300):
        im = self.preprocess(frames)
        preds = self.inference(im)
        results = self.postprocess(preds, conf_thres=conf, iou_thres=iou, agnostic=agnostic, max_det=max_det)
        return results

    def postprocess(self, preds, conf_thres=0.25, iou_thres=0.45, classes=None, agnostic=False, multi_label=False, labels=(), max_det=300, nc=0, max_time_img=0.05, max_nms=30000, max_wh=7680, in_place=True, rotated=False):
        xc = np.max(preds[:, 4: self.nc + 4], axis = 1) > conf_thres
        preds = np.transpose(preds, (0, 2, 1))
        preds[..., :4] = xywh2xyxy(preds[..., :4])
        x = preds[0][xc[0]]

        if not x.shape[0]:
          return None
        box, cls, keypoints = x[:, :4], x[:, 4:5], x[:, 5:]
        j = np.argmax(cls, axis=1)
        conf = cls[[i for i in range(len(j))], j]
        concatenated = np.concatenate((box, conf.reshape(-1, 1), j.reshape(-1, 1).astype(float), keypoints), axis=1)
        x = concatenated[conf.flatten() > conf_thres]

        if x.shape[0] > max_nms:
            x = x[x[:, 4].argsort(descending=True)[:max_nms]]
        cls = x[:, 5:6] * (0 if agnostic else max_wh)
        scores, boxes = x[:, 4], x[:, :4] + cls

        i = non_max_suppression(boxes, scores, iou_thres)
        return [x[i[:max_det]]]

    def inference(self, im):
        inputs = {key.name: value for key, value in zip(self.input_details, [im])}
        preds = self.session.run(self.output_details, inputs)[0]
        #preds[:, self.X_axis] *= im.shape[2] ; #preds[:, self.y_axis] *= im.shape[3]
        return preds

    def preprocess(self, im):
        im = np.stack(self.pre_transform(im))
        im = im[..., ::-1]
        im = np.ascontiguousarray(im).astype(np.float32)
        im /= 255.0
        im = np.transpose(im, (0, 3, 1, 2))
        return im

    def pre_transform(self, im):
        imgsz = self.input_details[0].shape[2:4]
        return [cv2.resize(im[0], imgsz, interpolation=cv2.INTER_LINEAR) for x in im]

class LetterBox:
    def __init__(self, new_shape=(640, 640), auto=False, scaleFill=False, scaleup=True, center=True, stride=32):
        self.new_shape = new_shape
        self.auto = auto
        self.scaleFill = scaleFill
        self.scaleup = scaleup
        self.stride = stride
        self.center = center

    def __call__(self, labels=None, image=None):
        if labels is None:
            labels = {}
        img = labels.get("img") if image is None else image
        shape = img.shape[:2]
        new_shape = labels.pop("rect_shape", self.new_shape)
        if isinstance(new_shape, int):
            new_shape = (new_shape, new_shape)

        r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
        if not self.scaleup:
            r = min(r, 1.0)

        ratio = r, r
        new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))
        dw, dh = new_shape[1] - new_unpad[0], new_shape[0] - new_unpad[1]
        if self.auto:
            dw, dh = np.mod(dw, self.stride), np.mod(dh, self.stride)
        elif self.scaleFill:
            dw, dh = 0.0, 0.0
            new_unpad = (new_shape[1], new_shape[0])
            ratio = new_shape[1] / shape[1], new_shape[0] / shape[0]

        if self.center:
            dw /= 2
            dh /= 2

        if shape[::-1] != new_unpad:
            img = cv2.resize(img, new_unpad, interpolation=cv2.INTER_LINEAR)
        top, bottom = int(round(dh - 0.1)) if self.center else 0, int(round(dh + 0.1))
        left, right = int(round(dw - 0.1)) if self.center else 0, int(round(dw + 0.1))
        img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=(114, 114, 114))
        if labels.get("ratio_pad"):
            labels["ratio_pad"] = (labels["ratio_pad"], (left, top))  # for evaluation

        if len(labels):
            labels = self._update_labels(labels, ratio, dw, dh)
            labels["img"] = img
            labels["resized_shape"] = new_shape
            return labels
        else:
            return img

    def _update_labels(self, labels, ratio, padw, padh):
        labels["instances"].convert_bbox(format="xyxy")
        labels["instances"].denormalize(*labels["img"].shape[:2][::-1])
        labels["instances"].scale(*ratio)
        labels["instances"].add_padding(padw, padh)
        return labels

def xywh2xyxy(x):
    assert x.shape[-1] == 4, f"input shape last dimension expected 4 but input shape is {x.shape}"
    y = np.empty_like(x)
    xy = x[..., :2]
    wh = x[..., 2:] / 2
    y[..., :2] = xy - wh
    y[..., 2:] = xy + wh
    return y

def non_max_suppression(boxes, scores, iou_threshold):
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]

    areas = (x2 - x1) * (y2 - y1)
    order = scores.argsort()[::-1]

    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])
        w = np.maximum(0.0, xx2 - xx1)
        h = np.maximum(0.0, yy2 - yy1)
        inter = w * h
        iou = inter / (areas[i] + areas[order[1:]] - inter)
        inds = np.where(iou <= iou_threshold)[0]
        order = order[inds + 1]

    return np.array(keep)

def plot(image, results, connections, visible = 0.1):
    for bboxes in results:
      x1, y1, x2, y2 = int(bboxes[0]), int(bboxes[1]), int(bboxes[2]), int(bboxes[3])
      conf, cls = bboxes[4] , bboxes[5]
      cv2.rectangle(image, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=3)
      cv2.putText(image, f'instance {conf:.2f}', (x1, y1 - 2), 0, 1, [0, 255, 0], thickness=2, lineType=cv2.LINE_AA)

      keypoints = bboxes[6:].reshape(-1, 3)
      for i in range(len(keypoints)):
        if keypoints[i][2] > visible:
          cv2.circle(image, (int(keypoints[i][0]), int(keypoints[i][1])), 5, (0, 255, 0), -1)

      for connection in connections:
        start_idx, end_idx = connection
        if start_idx < len(keypoints) and end_idx < len(keypoints):
          if keypoints[start_idx][2] > visible and keypoints[end_idx][2] > visible:
            cv2.line(image, (int(keypoints[start_idx][0]), int(keypoints[start_idx][1])), (int(keypoints[end_idx][0]), int(keypoints[end_idx][1])), (0, 255, 0), 2)
    return image
