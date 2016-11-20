from app.clarifai_cont.videoController import VideoController
from flask import render_template, request, jsonify
import json

from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/temp')
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('chart.html', values=values, labels=labels)

@app.route('/saveVideo', methods=['POST'])
def save_video():
	blob = request.data
	# imagen = open("./app/clarifai_cont/frame_images/user_video.mp4",'wb')
	imagen = open("./app/clarifai_cont/frame_images/testerWebcam.mp4",'wb')
	imagen.write(blob)
	imagen.close()
	
	return "Success"

@app.route('/getCharts', methods=['GET'])
def get_charts():
	video_obj = VideoController()
	data_set = video_obj.getDataFromVideo()
	print(data_set)
	print "Hey"
	return render_template('chart.html', dataset = data_set)




