import imageio
from videoProcessing import VideoProcessing
from clarifai_api import getProbabilityData
from convertVideo import ConvertVideo

class VideoController(object):
    def __init__(self):
        self.variable = 1
        self.vidProcess = VideoProcessing()

    def getDataFromVideo(self, name):
        ConvertVideo("../clarifai_cont/frame_images/" + name)
        imagePathList = self.readVideo("user_video_MP4.mp4")
        return self.getProbabilities(imagePathList)

    def readVideo(self, filename):
        #Handle conversion first
        readVideo = imageio.get_reader("../clarifai_cont/frame_images/" + filename)
        processedVid = self.vidProcess.processVid(readVideo)
        return processedVid

    def getProbabilities(self, imagePathList):
        return getProbabilityData(imagePathList)





# video_obj = VideoController()
# video_obj.getProbabilities()