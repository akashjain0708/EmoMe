import imageio
from app.clarifai_cont.videoProcessing import VideoProcessing
from app.clarifai_cont.clarifai_api import getProbabilityData
from app.clarifai_cont.convertVideo import ConvertVideo
# from app.clarifai_cont.cropFaces import CropImages

class VideoController(object):
    def __init__(self):
        self.variable = 1
        self.vidProcess = VideoProcessing()
        # self.imgCrop  = CropImages() 

    def getDataFromVideo(self, name=None):
        # ConvertVideo("../clarifai_cont/frame_images/" + name)
        imagePathList = self.readVideo("user_video.mp4")
        # imagePathList = self.readVideo("testerWebcam8.mp4")

        # self.imgCrop.cropFace(imagePathList)
        return self.getProbabilities(imagePathList)

    def readVideo(self, filename):
        #Handle conversion first
        readVideo = imageio.get_reader("./app/clarifai_cont/frame_images/" + filename)
        # readVideo = imageio.get_reader("./app/clarifai_cont/frame_images/testerWebcam8.mp4")
        processedVid = self.vidProcess.processVid(readVideo)
        return processedVid

    def getProbabilities(self, imagePathList):
        return getProbabilityData(imagePathList)





# video_obj = VideoController()
# video_obj.getProbabilities()