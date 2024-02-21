import torch
from PIL import Image
from yolov5 import YOLOv5

# 加载YOLOv5模型
model = YOLOv5('path/to/weights.pt', device='cuda')

# 读取集体照
image = Image.open('path/to/group_photo.jpg')

# 使用YOLOv5进行目标检测
results = model(image)

# 解析检测结果
persons = {}
for result in results:
    for det in result.boxes:
        label = det.get_field('label').item()
        if label not in persons:
            persons[label] = 0
        persons[label] += 1

# 输出统计结果
for person, count in persons.items():
    print(f'{person}: {count}')
