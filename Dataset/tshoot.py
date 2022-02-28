import os


def sanitize():
    path = 'Dataset/woman/Pack-1-YOLO/PACK-1-YOLO/'
    file_names = os.listdir(path)
    file_names.remove('classes.txt')

    for file_name in file_names:
        fin = open(path+file_name, "rt")
        fout = open("new_lanel/"+file_name, "wt")

        for line in fin:
            val = str(int(line[0:2])-15)
            line = val+" "+line[3:]
            fout.write(line)
            
        fin.close()
        fout.close()


def validate():
    path = 'Dataset/obj/'
    end = [0,1,2,3,4,5]
    file_names = os.listdir(path)
    file_names.remove('classes.txt')
    for file in file_names:
        if '.txt' in file:
            file = open(path+file, "rt")
            for line in file:
                if int(line[0:2]) not in end:
                    print(file)
                    print(line)
                    print()     
            file.close()           


def check_number():
    path = 'Dataset/obj/'
    files = os.listdir(path)
    files.remove('classes.txt')
    print(int(len(files)/2))

