import glob

fileList = glob.glob(r'C:\Users\EE803\Desktop\yolov7-main\datasets\paper_s_one_label\labels\train\*.txt')  #所有txt檔案

for file in fileList:
    with open(file) as f:
        for line in f.readlines():
            line_split = line.split(' ')
            if (line_split[0] != str(0)):
                print(file)
                
