import imageio
from videoProcessing import VideoProcessing

class VideoController(object):
	def __init__(self):
		self.variable = 1
		self.vidProcess = VideoProcessing()

	def readVideo(self, filename):
		readVideo = imageio.get_reader("assets/" + asfilename)
		processedVid = self.vidProcess.processVid(readVideo)
		
		return processedVid

	
v = VideoController()