from app import app
from flask import render_template, request
import urllib

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/temp')
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('chart.html', values=values, labels=labels)

@app.route('/submitData', methods=['POST'])
def post_chart_data():
    if request.method == 'POST':
        link_to_video = request.json
        testfile = urllib.URLopener()
        testfile.retrieve(link_to_video, "./clarifai_cont/frame_images/user_video.webm")

@app.route('/getChart', methods=['GET'])
def display_chart():
    video_obj = VideoController()
    data_set = video_obj.getProbabilityData('user_video.webm')
    return render_template('chart.html', values=values, labels=labels)
