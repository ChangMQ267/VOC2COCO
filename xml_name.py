import os
import xml.etree.ElementTree as ET
from datetime import datetime


def changeName(old_name):
    if old_name == 'fish-a' :
        return '红龙睛-a'
    if old_name == 'fish-b' :
        return '红龙睛-b'
    if old_name == 'fish-d' :
        return '红草金-d'
    if old_name == 'fish-c' :
        return '红草金-c'
    else:
        return old_name


if __name__ == '__main__':
    PATH = "E:/VOC/Annotations"
    SAVE_PATH = "E:/VOC/AnnotationsClean"
    timestart = datetime.now()
    if not os.path.isdir(SAVE_PATH):
        os.mkdir(SAVE_PATH)
    for (dirpath, dirnames, filenames) in os.walk(PATH):
        for filename in filenames:
            print(os.path.splitext(dirpath+filename)[1])
            if os.path.splitext(dirpath+filename)[1] != ".xml":
                continue
            tree = ET.parse(dirpath+"/"+filename)
            root = tree.getroot()
            # tarList = ["fish-a", "xmax", "ymin", "ymax"]
            # for tar in tarList:
            for index in root.iter("name"):
                print(index.text)
                index.text = changeName(index.text)
            tree.write(SAVE_PATH +"/"+ filename, encoding="UTF-8")
    print((datetime.now()-timestart))