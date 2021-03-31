import cv2
import os
from tqdm import tqdm

if __name__ == '__main__':

    sourceDir = 'E:/Workspaces/Data(20210320)/old_source'
    print(sourceDir)
    resultDir = "E:/Workspaces/Data(20210320)/source"
    print(resultDir)

    img_list = os.listdir(sourceDir)
    print(img_list)
    num = 1
    for img in img_list:
        pic = cv2.imread(os.path.join(sourceDir, img), cv2.IMREAD_COLOR)
        pic_n = cv2.resize(pic, (608, 456))
        pic_name = str(num)+".jpg"
        cv2.imwrite(os.path.join(resultDir, pic_name), pic_n)
        print(pic_name)
        num += 1
