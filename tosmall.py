# import xml.etree.cElementTree as et
# import cv2
#
#
# def read():
#     tree = et.parse("VOC/Annotations/IMG_0726.xml")
#     root = tree.getroot()
#     print(root)
#
#     fileName = root.find("filename").text  # 获取文件名
#
#     # 读取标注框信息
#     for obj in root.findall("object"):
#         name = obj.find("name").text
#         bndbox = obj.find("bndbox")
#         xmin = int(float(bndbox.find('xmin').text) - float(bndbox.find('xmin').text) % 1)
#         ymin = int(float(bndbox.find('ymin').text) - float(bndbox.find('ymin').text) % 1)
#         xmax = int(float(bndbox.find('xmax').text) - float(bndbox.find('xmax').text) % 1)
#         ymax = int(float(bndbox.find('ymax').text) - float(bndbox.find('ymax').text) % 1)
#         print(name, xmin, ymin, xmax, ymax)
#
#
# def phototosmall():
#     img = cv2.imread("./datasets/01/20190820094420.jpg")
#     height, weight = img.shape[:2]
#     x = 416 / weight  # 图片宽的缩放比例
#     y = 416 / height  # 图片稿的缩放比例
#     img = cv2.resize(img, (416, 416))
#
#     # xmin, ymin, xmax, ymax分别为xml读取的坐标信息
#     # tl = (int(xmin * x), int(ymin * y))
#     # br = (int(xmax * x), int(ymax * y))
#     cv2.rectangle(img, tl, br, (255, 0, 0), 1)
#
#
# if __name__ == '__main__':
#     read()