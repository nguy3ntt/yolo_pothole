def xyxy_to_xywh(box):
    x_min, y_min, x_max, y_max = box
    width = x_max - x_min
    height = y_max - y_min
    x_center = x_min + width / 2
    y_center = y_min + height / 2
    return (x_center, y_center, width, height)

def xywh_to_xyxy(box):
    x_center, y_center, width, height = box
    x_min = x_center - width / 2
    y_min = y_center - height / 2
    x_max = x_center + width / 2
    y_max = y_center + height / 2
    return (x_min, y_min, x_max, y_max)