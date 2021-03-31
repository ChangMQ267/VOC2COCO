### 将打标数据制作成训练集测试集

import os
import shutil
import numpy as np

# JPEGImages
# #work/PaddleDetection/dataset/roadsign_voc/valid.txt
# work/PaddleDetection/dataset/roadsign_voc/train.txt
# work/PaddleDetection/dataset/roadsign_voc/label_list.txt
# work/PaddleDetection/dataset/roadsign_voc/annotations
# work/PaddleDetection/dataset/roadsign_voc/images
# ./images/road218.png ./annotations/road218.xml
if __name__ == '__main__':
    PATH = "E:/Workspaces/VOC/"
    PhotoPath = PATH + "JPEGImages/"
    AnnoPath = PATH + "Annotations/"

    SAVE_PATH = "E:/Workspaces/VOC/dataset_voc/"
    imagesPath = SAVE_PATH + "images/"
    xmlPath = SAVE_PATH + "annotations/"

    os.mkdir(SAVE_PATH)
    os.mkdir(imagesPath)
    os.mkdir(xmlPath)

    t_v = 0.8  # 训练集/验证集     比 例

    valid_txt = []
    train_txt = []
    for (dirpath, dirnames, filenames) in os.walk(AnnoPath):
        filenum = len(filenames)
        i = 1
        for filename in filenames:
            photoname = filename.replace(".xml", ".jpg")
            print(photoname)
            if os.path.isfile(PhotoPath + photoname):
                shutil.move(PhotoPath + photoname, imagesPath)
                shutil.move(dirpath + filename, xmlPath)
                if i <= filenum * t_v:
                    train_txt.append(photoname.replace(".jpg", ""))
                else:
                    valid_txt.append(photoname.replace(".jpg", ""))
                i += 1
            else:
                print("No Image:" + filename)
    if len(valid_txt) == 0:
        print("valid_txt NULL")
    if len(train_txt) == 0:
        print("train_txt NULL")
    with open(SAVE_PATH + "/vaild.txt", 'w+', encoding='UTF-8') as v:
        for vaild1 in valid_txt:
            linestr = str("./images/" + vaild1 + ".jpg " + "./annotations/" + vaild1 + ".xml")
            v.write(linestr + "\n")
    with open(SAVE_PATH + "/train.txt", 'w+', encoding='UTF-8') as t:
        for train in train_txt:
            linestr = str("./images/" + train + ".jpg " + "./annotations/" + train + ".xml\n")
            t.write(linestr)
