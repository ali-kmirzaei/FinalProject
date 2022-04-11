import os
import glob
import random

image_list = glob.glob('data/newPack/*.jpg')
random.shuffle(image_list)
num = 1085

with open("train.txt", "w") as f:
    f.write("\n".join(image_list[:num]))
    # f.write("\n".join("\n"))

with open("test.txt", "w") as f:
    f.write("\n".join(image_list[num:]))
    # f.write("\n".join("\n"))
