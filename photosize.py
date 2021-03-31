from PIL import Image
from PIL import ImageFilter
import cv2
import time
import os
import numpy as np

#
# “”“代码中是将图片压缩到608X608，可以根据自己的需求修改”“”
im = Image.new("RGB", (608, 608), "white")  # 生成608X608的白色图片，可以根据自己的需求改变
imndarray = np.array(im)

path = "E:/Workspaces/Data(20210320)/source"  # 原图所在文件夹路径
path1 = path + "NEW"  # 处理完图片的保存路径
try:
    os.mkdir(path1)
except:
    print("bug")
filenames = os.listdir(path)

time1 = time.time()
for i in filenames:
    print(i)
    filename = os.path.join(path, i)
    filename1 = os.path.join(path1, i)
    # image = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), -1)
    img = Image.open(filename, "r")
    image = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    # 双三次插值
    height, width = image.shape[:2]  # 获取原图像的水平方向尺寸和垂直方向尺寸。
    temp = max(height, width)
    multemp = temp / 608
    if height > width:
        res = cv2.resize(image, (int(width / multemp), 608), interpolation=cv2.INTER_AREA)
    elif height < width:
        res = cv2.resize(image, (608, int(height / multemp)), interpolation=cv2.INTER_AREA)
    else:
        res = cv2.resize(image, (608, 608), interpolation=cv2.INTER_AREA)

    # 创建滤波器，使用不同的卷积核
    imgE = Image.fromarray(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
    gary2 = imgE.filter(ImageFilter.DETAIL)
    # #图像点运算
    gary3 = gary2.point(lambda i: i * 0.9)
    img_convert_ndarray = cv2.cvtColor(np.asarray(gary3), cv2.COLOR_RGB2BGR)
    height1, width1 = img_convert_ndarray.shape[:2]
    temph = int((608 - height1) / 2)
    tempw = int((608 - width1) / 2)
    a = cv2.copyMakeBorder(img_convert_ndarray, temph, 608 - temph - height1, tempw, 608 - tempw - width1,
                           cv2.BORDER_CONSTANT, value=[255, 255, 255])
    cv2.imencode('.jpg', a)[1].tofile(filename1)  # 保存图片
time2 = time.time()
print(u'总共耗时：' + str(time2 - time1) + 's')
