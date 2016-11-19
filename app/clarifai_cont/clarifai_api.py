from clarifai.rest import ClarifaiApp, Image as ClImage

app = ClarifaiApp()

model = app.models.get('Emotion')

image = ClImage(filename='./../static/assets/tester.jpg')

concept_details = model.predict([image])['outputs'][0]['data']['concepts'][0]
print concept_details['value']
print concept_details['name']