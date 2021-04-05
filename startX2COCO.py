import os


def startx2coco(PATH):
    NameTypes = ["train", "valid"]
    for NameType in NameTypes:
        voc_anno_dir = PATH + "/annotations"
        voc_anno_list = PATH + "/" + NameType + ".txt"
        voc_label_list = PATH + "/labels.txt"
        voc_out_name = PATH + "/annotations/" + NameType + ".json"
        cmdStr = "python x2coco.py --dataset_type voc --voc_anno_dir " + voc_anno_dir + " --voc_anno_list " + voc_anno_list + " --voc_label_list " + voc_label_list + " --voc_out_name " + voc_out_name
        os.system(cmdStr)


if __name__ == '__main__':
    PATH = "E:/VOC"
    # startx2coco(PATH)
    SAVE_PATH = PATH + "/dataset_voc/"

