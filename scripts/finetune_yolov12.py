"""
End-to-end script to fine-tune YOLOv12 model on the provided test dataset.
Assumes YOLOv12 training code is available and the dataset is in YOLO format.
"""
import os
from ultralytics import YOLO

# Paths
DATA_YAML = os.path.abspath('data.yaml')
TEST_IMAGES = os.path.abspath('test/images')
TEST_LABELS = os.path.abspath('test/labels')
MODEL_DIR = os.path.abspath('models')
OUTPUT_DIR = os.path.abspath('outputs')
LOGS_DIR = os.path.abspath('logs')

# Load a YOLOv8n model (downloads weights if not present)
model = YOLO("yolov8n.pt")  # Downloading YOLOv8 nano model

# Train the model on your dataset
results = model.train(data=DATA_YAML, epochs=50, imgsz=640, project=OUTPUT_DIR, name='yolov8-finetune')

# Example inference (optional):
# results = model('test/images/your_image.jpg')
# results.show()
