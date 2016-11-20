import imageio

class VideoProcessing(object):
	def __init__(self):
		pass

	def processVid(self, readVideo):
		fps = readVideo.get_meta_data()['fps']
		print("################", fps)
		stripFileNames = []
		count = 1
		try:
			for i, im in enumerate(readVideo):
				print("########", i)
				if i % int(fps) == 0:
					imageio.imwrite("./app/clarifai_cont/frame_images/temp" + str(count) + ".jpg", im)
					stripFileNames.append("temp" + str(count) + ".jpg")
					count += 1
			print("------------_ECRED --------")
		except RuntimeError:
			pass
		return stripFileNames
