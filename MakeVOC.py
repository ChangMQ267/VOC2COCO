### 将打标数据制作成训练集测试集

import os
import shutil
import numpy as np
from startX2COCO import startx2coco


# JPEGImages
# #work/PaddleDetection/dataset/roadsign_voc/valid.txt
# work/PaddleDetection/dataset/roadsign_voc/train.txt
# work/PaddleDetection/dataset/roadsign_voc/label_list.txt
# work/PaddleDetection/dataset/roadsign_voc/annotations
# work/PaddleDetection/dataset/roadsign_voc/images
# ./images/road218.png ./annotations/road218.xml
def mycopyfile(srcfile, dstpath):  # 复制函数
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        shutil.copy(srcfile, dstpath + fname)  # 复制文件
        print("copy %s -> %s" % (srcfile, dstpath + fname))


if __name__ == '__main__':
    PATH = "E:/VOC"
    PhotoPath = PATH + "/JPEGImages/"
    AnnoPath = PATH + "/Annotations/"

    SAVE_PATH = PATH + "/dataset_voc/"
    imagesPath = SAVE_PATH + "JPEGImages/"
    xmlPath = SAVE_PATH + "Annotations/"

    os.mkdir(SAVE_PATH)
    os.mkdir(imagesPath)
    os.mkdir(xmlPath)

    t_v = 0.8  # 训练集/验证集     比 例

    valid_txt = []
    train_txt = []
    with open(SAVE_PATH + "/valid.txt", 'w+', encoding='UTF-8') as v:
        with open(SAVE_PATH + "/train.txt", 'w+', encoding='UTF-8') as t:
            for (dirpath, dirnames, filenames) in os.walk(AnnoPath):
                filenum = len(filenames)
                i = 1
                for filename in filenames:
                    photoname = filename.replace(".xml", ".jpg")
                    print(photoname)
                    if os.path.isfile(PhotoPath + photoname):
                        mycopyfile(PhotoPath + photoname, imagesPath)
                        mycopyfile(dirpath + filename, xmlPath)
                        # shutil.move(PhotoPath + photoname, imagesPath)
                        # shutil.move(dirpath + filename, xmlPath)
                        if i <= filenum * t_v:
                            t.write(photoname.replace(".jpg", "") + "\n")
                            # train_txt.append(photoname.replace(".jpg", ""))
                        else:
                            v.write(photoname.replace(".jpg", "") + "\n")
                            # valid_txt.append(photoname.replace(".jpg", ""))
                        i += 1
                    else:
                        print("No Image:" + filename)

    with open(SAVE_PATH + "labels.txt", 'w+', encoding='UTF-8') as lN:
        with open(PATH + "/labels.txt", 'r+', encoding="utf-8") as lO:
            lN.write(lO.read())
    startx2coco(SAVE_PATH)  # 调用生成COCO数据集
    # if len(valid_txt) == 0:
    #     print("valid_txt NULL")
    # if len(train_txt) == 0:
    #     print("train_txt NULL")
    ##直接制作VOC数据集
    # with open(SAVE_PATH + "/valid.txt", 'w+', encoding='UTF-8') as v:
    #     for valid1 in valid_txt:
    #         linestr = str("./images/" + valid1 + ".jpg " + "./annotations/" + valid1 + ".xml")
    #         v.write(linestr + "\n")
    # with open(SAVE_PATH + "/train.txt", 'w+', encoding='UTF-8') as t:
    #     for train in train_txt:
    #         linestr = str("./images/" + train + ".jpg " + "./annotations/" + train + ".xml\n")
    #         t.write(linestr)
