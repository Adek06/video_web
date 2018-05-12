from flask import Flask, render_template, url_for
from app.tools import tools
import os
from flask import Flask, request, redirect, url_for


APP = Flask(__name__)
#APP.debug = True
my_port = 10001

@APP.route('/')
@APP.route('/hello/<name>')
def hello(name=None):
    if name == "OJBK":
        name = "ojbk"
    return render_template('hello.html', name=name)

video_dirc = {}
def link_id_video(id_range, video_ls):
    for video_id in id_range:
        video_dirc[video_id] = "http://{}:{}/static/files/video/{}".format(my_ip, my_port, video_ls[int(video_id)])

my_ip = tools.get_host_ip()
@APP.route('/files/')
def pic_list():
    video_ls = tools.get_files_url('./app/static/files/video/')
    video_id = [str(i) for i in range(len(video_ls))]
    link_id_video(video_id,video_ls)
    for url_str in video_ls:
        url_for('static', filename="files/video/"+url_str)
    return render_template('files.html', files_id=video_id, files_dirc=video_dirc, my_ip=my_ip)

@APP.route('/player/<video_id>')
def player(video_id):
    url = video_dirc[video_id]
    return render_template('player.html', url = url)

# APP.config['UPLOAD_FOLDER'] = "."

@APP.route('/uploads/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#           filename = secure_filename(file.filename)
#             file.save(os.path.join(APP.config['UPLOAD_FOLDER'], filename))
#             file_url = url_for('uploaded_file', filename=filename)
#         return html + '<br><img src=' + file_url + '>'
        file = request.files['file']
        filename = file.filename
        file.save("./app/static/files/video/upload/"+filename)
        #return "<h1>OK</h1"
    return render_template("upload.html")


if __name__ == "__main__":
    APP.run(debug=True, host='0.0.0.0', port=10001, threaded=True)
