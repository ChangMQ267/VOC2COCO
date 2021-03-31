import os
import cv2 as cv
import PIL
from tqdm import tqdm


# 1280*720
# (176,20,1130,720)

def cutPhoto(path, savepath):
    num = 1
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            photoPath = dirpath + "/" + filename
            img = cv.imread(photoPath)
            # img = PIL.Image.open(photoPath)
            # img2 = img.crop((176, 20, 1130, 720))
            img2 = img[0:1080, 250:1920]
            img2name = str(num) + ".jpg"
            url = savepath + "/" + img2name
            # img2.save(url)
            try:
                cv.imwrite(url, img2)
            except:
                print("bug")
            num += 1
            print(url)


if __name__ == '__main__':
    path = "videoPhoto/IMG_1263"
    savepath = "videoPhoto/IMG_1263/IMG_1263_CUT"
    try:
        os.mkdir(savepath)
    except:
        pass
    cutPhoto(path, savepath)
