from keras.models import load_model, Model
import matplotlib.pyplot as plt
import numpy as np

def view_filters(image_index, layer_index):
	model = load_model('Network.model')
	samples = np.load('samples.npy')
	samples = samples.astype('float32') / 255

	model.summary()

	layer_outputs = [layer.output for layer in model.layers]
	activation_model = Model(inputs=model.input, outputs=layer_outputs)
	activations = activation_model.predict(samples[image_index].reshape(1, 100, 100, 3))
	activation = activations[layer_index]

	print(np.array(activation).shape)

	fig, ax = plt.subplots(8, 8, figsize=(20, 20))
	index = 0
	for row in range(0, 8):
		for col in range(0, 8):
			ax[row][col].imshow(activation[0, :, :, index])
			index += 1
	plt.show()

view_filters(0, 7) # Image and Layer selection