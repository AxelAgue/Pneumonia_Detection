import glob, pylab, pandas as pd
import pydicom, numpy as np
import cv2


df = pd.read_csv('C:/Users/axel_/Desktop/Varios/DATASETS/RSNA/stage_1_train_labels.csv')

num_image = 28

patientId = df['patientId'][num_image]
dcm_file = 'C:/Users/axel_/Desktop/Varios/DATASETS/RSNA/train_images_2/%s.dcm' % patientId
dcm_data = pydicom.read_file(dcm_file)

image = dcm_data.pixel_array


x = df['x'][num_image]
y = df['y'][num_image]
width = df['width'][num_image]
height = df['height'][num_image]
Target = df['Target'][num_image]


def show_image(image, x, y, width, height, Target):
    if Target == 1:
        """
        xmin = int(x - width/2)
        ymin = int(y - height / 2)

        xmax = int(x + width/2)
        ymax = int(y + height / 2)
        """
        xmin = int(x)
        ymin = int(y)

        xmax = int(x + width)
        ymax = int(y + height)

        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)


show_image(image, x, y, width, height, Target)

cv2.imwrite("test1.jpg", image)
cv2.waitKey(0)
