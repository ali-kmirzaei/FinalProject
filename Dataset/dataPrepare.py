import os
import glob
import random

image_list = glob.glob('obj/*.jpg')
random.shuffle(image_list)
#print(image_list)
num = int(len(image_list)*70/100)
with open("train.txt", "w") as f:
    f.write("\n".join(image_list[:num]))

with open("test.txt", "w") as f:
    f.write("\n".join(image_list[num:]))


#cnt = 0
#trains = open('train.txt', "rt")
#tests = open('test.txt', "rt")
#for file in trains:
#    cnt += 1
#for file in tests:
#    cnt += 1
#print(cnt)
