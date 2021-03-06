from app.clarifai_cont.videoController import VideoController
from flask import render_template, request, jsonify
import json
import numpy as np

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
	imagen = open("./app/clarifai_cont/frame_images/user_video.mp4",'wb')
	# imagen = open("./app/clarifai_cont/frame_images/testerWebcam.mp4",'wb')
	imagen.write(blob)
	imagen.close()
	
	return "Success"


def getValues(data_set):
	returnData = {'Smile': [], 'sad': [], 'Anger': [], 'Fear': [], 'Surprise': []}
	for entry in data_set:
		for emotionEntry in data_set[entry]:
			returnData[emotionEntry].append(data_set[entry][emotionEntry])
	return returnData


def getMeanValues(smileValues, sadValues, angerValues, fearValues, surpriseValues):
	smileMean = np.mean(smileValues)
	sadMean = np.mean(sadValues)
	angerMean = np.mean(angerValues)
	fearMean = np.mean(fearValues)
	surpriseMean = np.mean(surpriseValues)

	meanOfMeans = (smileMean + sadMean + angerMean + fearMean + surpriseMean)/5

	print smileValues
	print smileMean
	print len(np.where(smileValues >= smileMean)[0])

	numAboveMeanSmile = len(np.where(smileValues > smileMean)[0])
	numAboveMeanSad = len(np.where(sadValues > sadMean)[0])
	numAboveMeanAnger = len(np.where(angerValues > angerMean)[0])
	numAboveMeanFear = len(np.where(fearValues > fearMean)[0])
	numAboveMeanSurprise = len(np.where(surpriseValues > surpriseMean)[0])

	percentageSmile = (smileMean*(float(numAboveMeanSmile)/len(smileValues))*100)/meanOfMeans
	percentageSad = (sadMean*(float(numAboveMeanSad)/len(sadValues))*100)/meanOfMeans
	percentageAnger = (angerMean*(float(numAboveMeanAnger)/len(angerValues))*100)/meanOfMeans
	percentageFear = (fearMean*(float(numAboveMeanFear)/len(fearValues))*100)/meanOfMeans
	percentageSurprise = (surpriseMean*(float(numAboveMeanSurprise)/len(surpriseValues))*100)/meanOfMeans

	return {'Smile': percentageSmile, 'sad': percentageSad, 'Anger': percentageAnger, 'Fear': percentageFear, 'Surprise': percentageSurprise}


def getHighestPerSecond(smileValues, sadValues, angerValues, fearValues, surpriseValues):
	smileMean = np.mean(smileValues)
	sadMean = np.mean(sadValues)
	angerMean = np.mean(angerValues)
	fearMean = np.mean(fearValues)
	surpriseMean = np.mean(surpriseValues)

	smileStd = np.std(smileValues)
	sadStd = np.std(sadValues)
	angerStd = np.std(angerValues)
	fearStd = np.std(fearValues)
	surpriseStd = np.std(surpriseValues)
	

	newSmileList = [(value - smileMean)/smileStd for value in smileValues]
	newSadList = [(value - sadMean)/sadStd for value in sadValues]
	newAngerList = [(value - angerMean)/angerStd for value in angerValues]
	newFearList = [(value - fearMean)/fearStd for value in fearValues]
	newSurpriseList = [(value - surpriseMean)/surpriseStd for value in surpriseValues]

	return {'Smile': newSmileList, 'sad': newSadList, 'Anger': newAngerList, 'Fear': newFearList, 'Surprise': newSurpriseList}


def getMeanIntensity(list):
	return float(sum ([x for x in list if x >= 0]))/len(list)


@app.route('/getCharts', methods=['GET'])
def get_charts():
	video_obj = VideoController()
	data_set = video_obj.getDataFromVideo()
	values = getValues(data_set)
	listOfPercentages = getMeanValues(values['Smile'], values['sad'], values['Anger'], values['Fear'], values['Surprise'])

	highestPerSecond = getHighestPerSecond(values['Smile'], values['sad'], values['Anger'], values['Fear'], values['Surprise'])

	meanOfIntensities = {'candidate' : {'Smile': getMeanIntensity(highestPerSecond['Smile']), 'sad': getMeanIntensity(highestPerSecond['sad']), 'Anger': getMeanIntensity(highestPerSecond['Anger']), 'Fear': getMeanIntensity(highestPerSecond['Fear']), 'Surprise': getMeanIntensity(highestPerSecond['Surprise'])}}



	print data_set
	print listOfPercentages
	print highestPerSecond
	print meanOfIntensities
	return render_template('chart.html', dataset = data_set, percentages = listOfPercentages, highestPerSecond = highestPerSecond)

@app.route('/charts', methods=['GET'])
def commonChart():
	return render_template('commonChart.html')



