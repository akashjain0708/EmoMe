import imageio

class VideoProcessing(object):
	def __init__(self):
		pass

	def processVid(self, readVideo):
		fps = readVideo.get_meta_data()['fps']

		stripFileNames = []
		count = 1
		for i, im in enumerate(readVideo):
			if i % fps == 0:
				imageio.imwrite("assets/splitImages/temp" + str(count) + ".jpg", im)
				stripFileNames.append("temp" + str(count) + ".jpg")
				count += 1

		return stripFileNames
