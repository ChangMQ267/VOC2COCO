import os
from datetime import datetime


def setnum():
    pass


# 图片命名格式化
if __name__ == '__main__':
    time1 = datetime.now()
    PATH = "Datalast_CUT"
    SAVE_PATH = "Datalast"
    if not os.path.isdir(SAVE_PATH):
        os.mkdir(SAVE_PATH)
    NUM_init = 9135  #自定义编号
    num = NUM_init
    for (dirpath, dirnames, filenames) in os.walk(PATH):
        dirpath = str(dirpath).replace("\\", "/")
        for file in filenames:
            reoldfile = dirpath + '/' + file
            # num = int(str(file).strip('.jpg'))
            # print(num)

            newfile = SAVE_PATH + "/fish" + str(num).zfill(6) + ".jpg"
            # newfile = str(SAVE_PATH+'/'+"fish","%4d"%num,".jpg")
            print(newfile)
            os.rename(reoldfile, newfile)
            num += 1
    time2 = datetime.now() - time1
    print(time2)
