import cv2
from utils.color_summarize import prep_image, color_analysis



image = cv2.imread('test.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

modified_image = prep_image(image)

color_analysis(modified_image)