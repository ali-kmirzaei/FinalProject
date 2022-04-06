import shutil
import Augmentor

def copy_trains():
    with open("data/train.txt", "rt") as f:
        trains = f.read().split('\n')
    trains.remove('')

    for img in trains:
        source = img
        destination = "data/objCopy/"+source[9:]
        shutil.copyfile(source, destination)


def do_aug():
    p = Augmentor.Pipeline("data/empty")

    # p.rotate(1, 25, 25)
    p.skew(1)
    p.sample(100)



do_aug()