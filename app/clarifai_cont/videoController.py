import imageio
from videoProcessing import VideoProcessing
from clarifai_api import *

class VideoController(object):
    def __init__(self):
        self.variable = 1
        self.vidProcess = VideoProcessing()

    def readVideo(self, filename):
        #Handle conversion first
        readVideo = imageio.get_reader("../clarifai_cont/frame_images/" + filename)
        processedVid = self.vidProcess.processVid(readVideo)
        return processedVid

    def getProbabilities(self):
        frame_image_path_list = self.readVideo("user_video_MP4.mp4")
        getProbabilityData(frame_image_path_list)


video_obj = VideoController()
video_obj.getProbabilities()