from moviepy.editor import *

class ConvertVideo(object):
	def __init__(self):
		pass

	def convertWebmToMp4(self, givenFile):
		myClip = VideoFileClip(givenFile)
		myClip.write_videofile(givenFile[:givenFile.find('.')] + ".mp4")