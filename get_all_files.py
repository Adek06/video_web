import os 

def get_files_url(dir):
    files_generator = os.walk(dir)
    files_list = []
    for i in files_generator:
        for j in i[2]:
            x = "{}/{}".format(i[0], j)#[21:]
            files_list.append(x)
            # files_list.append(x[20:][2:])
    return files_list
def get_2(dir):
    return os.listdir(str(dir))
pic_ls = get_files_url('./static/files/video/')
#pic_ls2 = get_2('./static/files/video/')

for i in pic_ls:
    print(i)
#print(pic_ls2)