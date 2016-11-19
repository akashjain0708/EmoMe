from clarifai.rest import ClarifaiApp

app = ClarifaiApp()

model = app.models.get('general-v1.3')

print model.predict_by_url('https://samples.clarifai.com/metro-north.jpg')