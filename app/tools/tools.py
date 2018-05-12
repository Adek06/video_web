import os

def get_files_url(dir):
    files_generator = os.walk(dir)
    files_list = []
    for i in files_generator:
        for j in i[2]:
            if ".mp4" in j[-5:] or ".m4a" in j[-5:] or ".mp3" in j[-5:]:
                x = "{}/{}".format(i[0], j)[25:]
                files_list.append(x)
    return files_list

import socket
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip