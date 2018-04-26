import os

local_url = "./static/files/video/Movie/怪奇物语S02.Stranger.Things.2017.1080p.WEB-DL.x265.AC3￡cXcY@FRDS/"
os.chdir(local_url)
need_trans_ls = os.listdir("./")
x = [str(i) for i in need_trans_ls if (".flv" in i) or (".mkv" in i) or (".wmv" in i)]
mod = None
# if ".wmv" in x[0]:
#     mod = 'wmv'
print("x is {}".format(x))
def add_xie(file_name):
    new = ""
    for i in file_name:
        g = ''
        if i == " ":
            g = "\\ "
        elif i == "(":
            g = "\\("
        elif i == ")":
            g = "\\)"
        elif i == "[":
            g = "\\["
        elif i == "]":
            g = "\\]"
        elif i == "&":
            g = "\\&"
        else:
            g = i
        new += g
    return new
try:
    name_font,name_Extension = add_xie(x[0]).split('.')
except ValueError:
    if ".mkv" in x[0]:
        name_font = add_xie(x[0])[0:-4]
        name_Extension = add_xie(x[0])[-3:]
for i in x:
    try:
        name_first, name_last = add_xie(i).split('.')
    except ValueError:
        if ".mkv" in i:
            name_first = add_xie(i)[0:-4]
            name_last = add_xie(i)[-3:]
    if mod == "wmv":
        recommend = "ffmpeg -i {} -y -vcodec libx264 -acodec aac -strict -2 {}.mp4".format(name_first+"."+name_last, name_first)
    else:
        recommend = "ffmpeg -i {} -y -vcodec copy -acodec copy {}.mp4".format(name_first+"."+name_last, name_first)
    print(recommend)
    os.system(recommend)
os.system(r"mkdir {name_font}".format(name_font=name_font))
os.system(r"mv *.{name_last} {name_font}/".format(name_last=name_last, name_font=name_font))
os.system(r"zip -r {name_font1}.zip {name_font}/".format(name_font1=name_font, name_font=name_font))






