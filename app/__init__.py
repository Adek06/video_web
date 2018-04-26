from flask import Flask, render_template, url_for
import os

APP = Flask(__name__)
APP.debug = True

@APP.route('/')
@APP.route('/hello/<name>')
def hello(name=None):
    if name == "OJBK":
        name = "ojbk"
    return render_template('hello.html', name=name)

import socket
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
my_ip = get_host_ip()

def get_files_url(dir):
    files_generator = os.walk(dir)
    files_list = []
    for i in files_generator:
        for j in i[2]:
            if ".mp4" in j[-5:]:
                x = "{}/{}".format(i[0], j)[24:]
                files_list.append(x)
            # files_list.append(x[20:][2:])
    return files_list

video_dirc = {}
def link_id_video(id_range, video_ls):
    for video_id in id_range:
        video_dirc[video_id] = "http://{}:10001/static/files/video/{}".format(my_ip, video_ls[int(video_id)])

@APP.route('/files/')
def pic_list():
    video_ls = get_files_url('./app/static/files/video/')
    video_id = [str(i) for i in range(len(video_ls))]
    link_id_video(video_id,video_ls)
    for url_str in video_ls:
        url_for('static', filename="files/video/"+url_str)
    return render_template('files.html', files_id=video_id, files_dirc=video_dirc, my_ip=my_ip)

@APP.route('/player/<video_id>')
def player(video_id):
    url = video_dirc[video_id]
    return render_template('player.html', url = url)

if __name__ == "__main__":
    APP.run(debug=True, host='0.0.0.0', port=10001, threaded=True)
