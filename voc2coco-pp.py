import os
from tqdm import tqdm
import xml.etree.ElementTree as ET
import json


def voc2coco(data_dir, train_file, test_file):
    xml_dir = os.path.join(data_dir, 'Annotations')
    img_dir = os.path.join(data_dir, 'JPEGImages')

    with open(train_file, 'r') as f:
        train_fs = f.readlines()
    # train_xmls = [os.path.join(xml_dir, n.strip() + '.xml') for n in train_fs]
    train_xmls = [os.path.join(xml_dir, n.strip()) for n in train_fs]
    print(train_xmls)
    with open(test_file, 'r') as f:
        test_fs = f.readlines()
    test_xmls = [os.path.join(xml_dir, n.strip()) for n in test_fs]
    print('got xmls')
    train_coco = xml2coco(train_xmls)
    test_coco = xml2coco(test_xmls)
    with open(os.path.join(data_dir, 'coco_train.json'), 'w') as f:
        json.dump(train_coco, f, ensure_ascii=False, indent=2)
    with open(os.path.join(data_dir, 'coco_test.json'), 'w') as f:
        json.dump(test_coco, f, ensure_ascii=False, indent=2)
    print('done')


def xml2coco(xmls):
    pass


if __name__ == '__main__':
    data_dir = ""
    train_file = ""
    test_file = ""
    voc2coco(data_dir, train_file, test_file)
