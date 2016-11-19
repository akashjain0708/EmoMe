from app import app
from flask import render_template, request
import urllib
from clarifai_cont.videoController import VideoController

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/temp')
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('chart.html', values=values, labels=labels)

@app.route('/getCharts', methods=['GET'])
def get_charts():
    data_set = []
    if request.method == 'GET':
        link_to_video = request.json['videoURL']
        testfile = urllib.URLopener()
        testfile.retrieve(link_to_video, "./clarifai_cont/frame_images/user_video.webm")
        video_obj = VideoController()
        data_set = video_obj.getDataFromVideo('user_video.webm')
    return render_template('chart.html', dataset = data_set)
