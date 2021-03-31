import os
from tqdm import tqdm


def txtreplace(line):
    str = line.replace(".JPG", "")
    str = str.replace(".jpg", "")
    str = str.replace(" 1", "")
    str = str.replace(" -1", "")
    str = str.replace("\n", "")
    return str


def txt2train(path):
    print("Trainval")
    with open((path+"trainval.txt"), 'w+') as t:
        with open((path + "fish-a_train.txt"), 'r') as f:
            for line in f.readlines():
                # ./ images / road218.png. / annotations / road218.xml
                # str = line.strip(".JPG 1\n")
                str = txtreplace(line)
                print(str)
                t.write(str+"\n")
                # t.write("./JPRGImages/" + str + ".JPG ./Annotations/" + str + ".xml\n")
                # t.write(str+"\n")

    # train_xmls = [os.path.join(xml_dir, n.strip() + '.xml') for n in train_fs]


def txt2test(path):
    print("Test")
    with open((path+"test.txt"), 'w+') as t:
        with open((path + "fish-a_val.txt"), 'r') as f:
            for line in f.readlines():
                # ./ images / road218.png. / annotations / road218.xml
                # str = line.strip(".JPG 1\n")
                str = txtreplace(line)
                print(str)
                # t.write("./JPRGImages/" + str + ".JPG ./Annotations/" + str + ".xml\n")
                # t.write("./JPRGImages/" + str + "\n")
                t.write(str+"\n")


if __name__ == '__main__':
    data_dir = "C:/Users/chang/Desktop/Fish-PascalVOC-export/ImageSets/Main/"
    txt2train(data_dir)
    txt2test(data_dir)
