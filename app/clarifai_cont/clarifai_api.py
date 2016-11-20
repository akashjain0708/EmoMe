from clarifai.rest import ClarifaiApp, Image as ClImage
app = ClarifaiApp()

def getProbabilityData(files=None):
	model = app.models.get('Emotion')

	for index, file_path in enumerate(files):
		files[index] = ClImage(filename='./app/clarifai_cont/frame_images/'+file_path);


	temp = model.predict(files)
	print temp
	concept_details = temp['outputs']

	graph_result = {}

	# {1: {'Smile':0.5, 'Sad': 0.9}, 2: }
	# for index in range(0, len(concept_details)):
	# 	each_element = []
	# 	for concept_index in range(0, len(concept_details[index]['data']['concepts'])):
	# 		name = concept_details[index]['data']['concepts'][concept_index]['name']
	# 		value = concept_details[index]['data']['concepts'][concept_index]['value']
	# 		each_element.append({name: value})
	# 	graph_result.append({index: each_element})

	for index in range(0, len(concept_details)):
		each_element = {}
		for concept_index in range(0, len(concept_details[index]['data']['concepts'])):
			name = concept_details[index]['data']['concepts'][concept_index]['name']
			value = concept_details[index]['data']['concepts'][concept_index]['value']
			each_element[name] = value
		graph_result[index] = each_element



	print graph_result
	return graph_result

	# concept_details = model.predict([image, image2])['outputs'][0]['data']['concepts'][0]