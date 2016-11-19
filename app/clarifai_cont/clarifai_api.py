from clarifai.rest import ClarifaiApp, Image as ClImage
app = ClarifaiApp()

def getProbabilityData(files=None):
	model = app.models.get('Emotion')

	for index, file_path in enumerate(files):
		files[index] = ClImage(filename='./frame_images/'+file_path);

	concept_details = model.predict(files)['outputs']

	graph_result = []

	for index in range(0, len(concept_details)):
		each_element = []
		for concept_index in range(0, len(concept_details[index]['data']['concepts'])):
			name = concept_details[index]['data']['concepts'][concept_index]['name']
			value = concept_details[index]['data']['concepts'][concept_index]['value']
			each_element.append({name: value})
		graph_result.append({index: each_element})

	print graph_result
	return graph_result

	# concept_details = model.predict([image, image2])['outputs'][0]['data']['concepts'][0]