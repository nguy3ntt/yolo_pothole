import numpy as np
from src.fundamentals.iou import compute_iou

def nms(boxes, scores, iou_threshold=0.5):
    boxes = np.array(boxes)
    scores = np.array(scores)

    order = scores.argsort()[::-1]
    keep = []

    while len(order) > 0:
        current = order[0]
        keep.append(current)

        remaining = []
        for idx in order[1:]:
            iou = compute_iou(boxes[current], boxes[idx])
            if iou < iou_threshold:
                remaining.append(idx)

        order = np.array(remaining)

    return keep