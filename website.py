from flask import Flask
from flask import render_template
from flask import request
import os
from tempfile import NamedTemporaryFile
import urllib.request
import subprocess
import time

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def homepage():

    url, img = '', ''

    if request.method == 'POST':

        try:
            url = request.form['url']
            img = capturing(url)
            print(img)
            return render_template('selection.html', url=url, img=img)
        except KeyError as err:
            print(err)


    print('-', url, img)

    return render_template('index.html')



def capturing(url):
    """
    http://www.draketo.de/english/download-web-page-with-all-prerequisites
    """
    print('capturing started...')

    phantomJS = 'C:\\Users\\roland\\Desktop\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'
    captureJS = 'C:\\Users\\roland\\PycharmProjects\\HoE\\static\\js\\capture.js'
    tmpDIR = 'C:\\Users\\roland\\PycharmProjects\\HoE\\temp\\'

    with NamedTemporaryFile(dir=tmpDIR) as tf:
        fname = tf.name + '.png'
        img = 'http://localhost:45678/' + fname.rsplit('\\')[-1]

    command = '{} {} {} {}'.format(phantomJS, captureJS, url, fname)
    subprocess.call(command, shell=True)

    print('capturing ended')
    return img


if __name__ == "__main__":
    app.debug = True
    app.run()
