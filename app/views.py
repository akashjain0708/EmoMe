from app.clarifai_cont.videoController import VideoController
from flask import render_template, request

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

@app.route('/getCharts', methods=['POST'])
def get_charts_2():
	blob = request.data
	imagen = open("./app/clarifai_cont/frame_images/user_video.mp4",'wb')
	imagen.write(blob)
	imagen.close()
	
	video_obj = VideoController()
	data_set = video_obj.getDataFromVideo()
	return render_template('chart.html', dataset = data_set)




