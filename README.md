# ONNX YOLOv5 Instance Segmentation
 Python scripts performing instance segmentation using the YOLOv5 model in ONNX.

![! ONNX YOLOv5 Instance Segmentation](https://github.com/ibaiGorordo/ONNX-YOLOv5-Instance-Segmentation/blob/main/doc/img/detected_objects.jpg)
*Original image: https://www.flickr.com/photos/nicolelee/19041780*

# Important
- The input images are directly resized to match the input size of the model. I skipped adding the pad to the input image (image letterbox), it might affect the accuracy of the model if the input image has a different aspect ratio compared to the input size of the model. Always try to get an input size with a ratio close to the input images you will use.

# Requirements

 * Check the **requirements.txt** file.
 * For ONNX, if you have a NVIDIA GPU, then install the **onnxruntime-gpu**, otherwise use the **onnxruntime** library.

# Installation
```
git clone https://github.com/ibaiGorordo/ONNX-YOLOv5-Instance-Segmentation.git
cd ONNX-YOLOv5-Instance-Segmentation
pip install -r requirements.txt
```
### ONNX Runtime
For Nvidia GPU computers:
`pip install onnxruntime-gpu`

Otherwise:
`pip install onnxruntime`

# ONNX model
You can convert the Pytorch model to ONNX using the following Google Colab notebook:  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-WRAk_KbdG511xxg-rjYBNYo3FrH2-u_?usp=sharing)
- The License of the models is GPL-3.0 license: [License](https://github.com/ultralytics/yolov5/blob/master/LICENSE)

# Original YOLOv5 model
The original YOLOv5 Instance Segmentation model can be found in this repository: [YOLOv5 Instance Segmentation](https://github.com/ultralytics/yolov5)

# Examples

 * **Image inference**:
 ```
 python image_instance_segmentation.py
 ```

 * **Webcam inference**:
 ```
 python webcam_instance_segmentation.py
 ```

 * **Video inference**: https://youtu.be/p2iUTSiZBas
 ```
 python video_instance_segmentation.py
 ```
 ![!YOLOv5 instance segmentation video](https://github.com/ibaiGorordo/ONNX-YOLOv5-Instance-Segmentation/blob/main/doc/img/video_yolo_segmentation.gif)

# References:
* YOLOv5 model: https://github.com/ultralytics/yolov5
* yolov5-seg-opencv-onnxruntime-cpp: https://github.com/UNeedCryDear/yolov5-seg-opencv-onnxruntime-cpp
* PINTO0309's model zoo: https://github.com/PINTO0309/PINTO_model_zoo
* PINTO0309's model conversion tool: https://github.com/PINTO0309/openvino2tensorflow
