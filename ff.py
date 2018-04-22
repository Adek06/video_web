import os

need_ls = os.listdir("./")
x = [str(i) for i in need_ls if (".flv" in i) or (".mkv" in i)]
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
name_font,name_last = add_xie(x[0]).split('.')
for i in x:
    name_first, name_last = add_xie(i).split('.')
    commond = "ffmpeg -i {} -y -vcodec copy -acodec copy {}.mp4".format(name_first+"."+name_last, name_first)
    print(commond)
    os.system(commond)
os.system(r"mkdir {name_font}".format(name_font=name_font))
os.system(r"mv *.{name_last} {name_font}/".format(name_last=name_last, name_font=name_font))
os.system(r"zip -r {name_font1}.zip {name_font}/".format(name_font1=name_font, name_font=name_font))






