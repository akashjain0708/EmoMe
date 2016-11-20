import cv2
import os 

class CropImages():
	def __init__(self):
		pass

	def cropFace(self,imagePathList):
		faceCascade = cv2.CascadeClassifier('abc.xml')
		print str(faceCascade)

		print "################################################"
		print "HEY"


		imagePathList = ['temp2.jpg', 'temp3.jpg', 'temp4.jpg', 'temp5.jpg', 'temp6.jpg',
							'temp7.jpg', 'temp8.jpg', 'temp9.jpg']

		# imagePath = imagePathList[2]
		#red image
		for imagePath in imagePathList:
			print imagePath
			# image = cv2.imread('./app/clarifai_cont/frame_images/' + imagePath)
			image = cv2.imread('./frame_images/' + imagePath)
			print os.path.exists('./frame_images/' + imagePath)
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			# cv2.imshow('gry', gray)
			# cv2.waitKey(0)
			# cv2.destroyAllWindows()
			# faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

			faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
			print str(faces)

			for (x, y, w, h) in faces:
				print imagePath
				img = image[y-50:y+h+50,x-50:x+w+50]
				# cv2.imshow('img',img)
				# cv2.waitKey(0)
				# cv2.destroyAllWindows()
				# cv2.imwrite('./app/clarifai_cont/frame_images/' + imagePath, img)
				cv2.imwrite('./frame_images/' + imagePath, img)

			print "################################################"

c = CropImages()
c.cropFace([])