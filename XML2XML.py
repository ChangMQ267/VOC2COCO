import os
import xml.etree.ElementTree as ET




#<folder>JPEGImages</folder>
#
# <filename>fish000001.jpg</filename>
#
# <path>C:\Users\501\Desktop\VOC\JPEGImages\fish000001.jpg</path>

if __name__ == '__main__':
    PATH = "C:/Users/chang/Desktop/Fish-PascalVOC-export/Annotations/"
    SAVE_PATH = "C:/Users/chang/Desktop/Fish-PascalVOC-export/AnnotationsClean/"
    if not os.path.isdir(SAVE_PATH):
        os.mkdir(SAVE_PATH)
    for (dirpath, dirnames, filenames) in os.walk(PATH):
        for filename in filenames:
            print(os.path.splitext(dirpath+filename)[1])
            if os.path.splitext(dirpath+filename)[1] != ".xml":
                continue

            try:
                num = int(str(filename).replace(".xml", ""))
            except:
                print("bug")
                continue
            filename_new = "fish"+str(num).zfill(6)+".xml"
            path_new = "C:\\Users\\501\\Desktop\\VOC\\JPEGImages\\"+filename_new
            tree = ET.parse(dirpath+filename)
            root = tree.getroot()
            tarList = ["folder","filename","path","name"]
            for tar in tarList:
                for index in root.iter(tar):
                    if tar == tarList[0]:
                       text = "JPEGImages"
                       index.text = text
                    elif tar == tarList[1]:
                        index.text = filename_new
                    elif tar == tarList[2]:
                        index.text = path_new
                    elif tar == tarList[3]:
                        index.text = str.lower(index.text)
                    print(index.text)
            #         #num = float2int(index.text)
            #         index.text = str(num)
            tree.write(SAVE_PATH + filename_new, encoding="UTF-8")
