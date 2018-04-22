import os 

def get_files(dir):
    files_generator = os.walk(dir)
    files_list = []
    for i in files_generator:
        for j in i[2]:
            x = "{}/{}".format(i[0], j)
            x = x[20:]
            print(x.split(".mp4")[0])
            files_list.append(x)
    return files_list
def get_2(dir):
    return os.listdir(str(dir))
pic_ls = get_files('./static/files/video/')
#pic_ls2 = get_2('./static/files/video/')

#print(pic_ls)
#print(pic_ls2)