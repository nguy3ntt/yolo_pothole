# YOLO Pothole Detection

An end-to-end YOLO object detection project for pothole detection, covering detection fundamentals, annotation conversion, training, evaluation, and inference

## Project Goal

This project is designed to build both conceptual and practical understanding of object detection.  
It begins with the fundamentals of bounding boxes, IoU, and Non-Max Suppression, then progresses to training a real YOLO model on a pothole detection dataset

## Structure

```
yolo-pothole-detection/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   ├── interim/
│   ├── yolo_format/
│   └── splits/
│
├── notebooks/
│   ├── 01_foundations_bbox_iou_nms.ipynb
│   ├── 02_dataset_understanding.ipynb
│   ├── 03_annotation_conversion.ipynb
│   ├── 04_yolo_training.ipynb
│   ├── 05_evaluation.ipynb
│   └── 06_inference_demo.ipynb
│
├── src/
│   ├── fundamentals/
│   │   ├── bbox_utils.py
│   │   ├── iou.py
│   │   └── nms.py
│   │
│   ├── data/
│   │   ├── load_dataset.py
│   │   ├── convert_voc_to_yolo.py
│   │   ├── split_dataset.py
│   │   └── validate_labels.py
│   │
│   ├── yolo_pipeline/
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   ├── predict.py
│   │   └── dataset.yaml
│   │
│   └── utils/
│       ├── visualization.py
│       └── paths.py
│
├── runs/
│   ├── train/
│   └── predict/
│
├── assets/
│   ├── sample_images/
│   ├── bbox_examples/
│   ├── predictions/
│   └── plots/
│
└── reports/
    └── results.md
```