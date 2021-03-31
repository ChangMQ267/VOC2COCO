import os
import shutil


def findPhoto(PHOTOPATH, filename, SAVE_PATH):
    filename_1 = str(filename).strip(".xml")
    photourl = PHOTOPATH + filename_1 + ".jpg"
    if (os.path.exists(photourl)):
        shutil.move(photourl, SAVE_PATH)
    else:
        print(filename)


def findXML(PATH, XMLPATH):
    i = 0
    train = 0.8

    for (dirpath, dirnames, filenames) in os.walk(PATH):
        print(len(filenames))
        with open((XMLPATH + "trainval.txt"), 'w+') as tr:
            with open((XMLPATH + "test.txt"), 'w+') as te:
                for filename in filenames:
                    filename = str(filename).strip(".xml")
                    if i < len(filenames) * train:
                        tr.write(filename + "\n")
                    else:
                        te.write(filename + "\n")
                    i += 1


if __name__ == '__main__':
    PATH = "C:/Users/chang/Desktop/Fish-PascalVOC-export/Annotations/"
    XMLPATH = "C:/Users/chang/Desktop/Fish-PascalVOC-export/ImageSets/Main/"
    SAVE_PATH = "C:/Users/chang/Desktop/Fish-PascalVOC-export/images/"
    PHOTOPATH = "C:/Users/chang/Desktop/Fish-PascalVOC-export/JPEGImages/"
    # for (dirpath, dirnames, filenames) in os.walk(PATH):
    #     for filename in filenames:
    #         findPhoto(PHOTOPATH,filename,SAVE_PATH)
    findXML(PATH, XMLPATH)
