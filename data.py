import torch
from PIL import Image, ImageDraw
import os
import PIL
import pandas as pd

model = torch.hub.load('ultralytics/yolov5', 'custom', path='./weights/best.pt')

def detect_and_save_annotated_image(image_path, output_path):
    img = Image.open(image_path)
    results = model(img)  
    
    bboxes = results.pred[0][:, :4] 
    confidences = results.pred[0][:, 4]  # get the confidence scores
    
    total_area_covered = 0
    x1, y1, x2, y2 = 0, 0, 0, 0
    
    draw = ImageDraw.Draw(img)
    for bbox, confidence in zip(bboxes, confidences):
        # if confidence > 20:  # only draw the box if confidence is above 20
        x1, y1, x2, y2 = bbox.int().tolist()
        
        for i in range(x1, x2, 4):
            draw.line([(i, y1), (i + 2, y1)], fill="black", width=3)
            draw.line([(i, y2), (i + 2, y2)], fill="black", width=3)
        for i in range(y1, y2, 4):
            draw.line([(x1, i), (x1, i + 2)], fill="black", width=3)
            draw.line([(x2, i), (x2, i + 2)], fill="black", width=3)
            
            total_area_covered += (x2 - x1) * (y2 - y1)

    img.save(output_path)

    num_bboxes = len(bboxes)
    total_available_area = img.height * img.width

    x_dim = x2 - x1
    y_dim = y2 - y1
    
    #coverage_percentage = (total_area_covered / total_available_area) * 100
    return num_bboxes, total_area_covered, total_available_area, x_dim, y_dim


data = os.listdir('./iot/')
boxes = []
box_area = []
tot_area = []
name_of_plot = []
x_dims = []
y_dims = []
for enum, i in enumerate(data):
    num_bboxes, coverage_percentage, total_available_area, x_dim, y_dim =  detect_and_save_annotated_image('./contour_images/'+i, f'./detected_contour_images/{i}')
    boxes.append(num_bboxes)
    box_area.append(coverage_percentage)
    tot_area.append(total_available_area)
    name_of_plot.append('./detected_contour_images/'+i)
    x_dims.append(x_dim)
    y_dims.append(y_dim)