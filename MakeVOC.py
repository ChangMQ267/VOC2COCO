### 将打标数据制作成训练集测试集

import os


#JPEGImages
# #work/PaddleDetection/dataset/roadsign_voc/valid.txt
# work/PaddleDetection/dataset/roadsign_voc/train.txt
# work/PaddleDetection/dataset/roadsign_voc/label_list.txt
# work/PaddleDetection/dataset/roadsign_voc/annotations
# work/PaddleDetection/dataset/roadsign_voc/images
#./images/road218.png ./annotations/road218.xml
if __name__ == '__main__':
    PATH = "E:/Workspaces/VOC/"
    SAVE_PATH = "E:/Workspaces/VOC/dataset_voc"
    if not os.path.isdir(SAVE_PATH):
        os.mkdir(SAVE_PATH)
    for (dirpath, dirnames, filenames) in os.walk(PATH+"Annotations"):
        for filename in filenames:

            print(filename)