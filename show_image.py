import cv2
from PIL import Image

def show_image(image,path):
    if path!='':
        image=Image.open(path)
    cv2.imshow('image', image)
    while(1):
        if cv2.waitKey(10)&0xFF==27: # If it is 64 bit processor, then only use 0xFF otherwise don't
            break
    cv2.destroyAllWindows()
