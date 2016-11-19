from clarifai.rest import ClarifaiApp, Image as ClImage

app = ClarifaiApp()

model = app.models.get('Emotion')

# image = ClImage(filename='/assets/tester.jpg')

print model.predict_by_url('https://samples.clarifai.com/metro-north.jpg')