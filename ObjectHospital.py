import os
import xml.etree.ElementTree as ET

def hospital(dirpath,filename):
    tree = ET.parse(dirpath+filename)
    tree.find("annotation")


if __name__ == '__main__':
    PATH = "C:/Users/chang/Desktop/Fish-PascalVOC-export/Annotations/"
    SAVE_PATH = "C:/Users/chang/Desktop/Fish-PascalVOC-export/AnnotationsClean/"
    if not os.path.isdir(SAVE_PATH):
        os.mkdir(SAVE_PATH)
    for (dirpath, dirnames, filenames) in os.walk(PATH):
        for filename in filenames:
            print(os.path.splitext(dirpath + filename)[1])
            if os.path.splitext(dirpath + filename)[1] != ".xml":
                continue

            # tarList = ["xmin", "xmax", "ymin", "ymax"]
            # for tar in tarList:
            #     for index in root.iter(tar):
            #         print(index.text)
            #         num = float2int(index.text)
            #         index.text = str(num)
            # tree.write(SAVE_PATH + filename, encoding="UTF-8")