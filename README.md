# Gesture-Recognition-CNN
Convolutional Neural Network that can recognize between 10 different types of hand gestures with an accuracy ~99% after 5 epochs using [Tensorflow](https://www.tensorflow.org/).

## Dependencies 
[Dataset](https://www.kaggle.com/gti-upm/leapgestrecog)
```bash 
pip install tensorflow
```

## Usage
Simply extract leapGestRecog next to the script and then run it.

## Model Summary
When using an image size of 100x100
```bash
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 98, 98, 64)        1792      
_________________________________________________________________
activation_1 (Activation)    (None, 98, 98, 64)        0         
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 49, 49, 64)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 47, 47, 128)       73856     
_________________________________________________________________
activation_2 (Activation)    (None, 47, 47, 128)       0         
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 23, 23, 128)       0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 21, 21, 128)       147584    
_________________________________________________________________
activation_3 (Activation)    (None, 21, 21, 128)       0         
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 10, 10, 128)       0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 12800)             0         
_________________________________________________________________
dense_1 (Dense)              (None, 10)                128010    
_________________________________________________________________
activation_4 (Activation)    (None, 10)                0         
=================================================================
Total params: 351,242
Trainable params: 351,242
Non-trainable params: 0
_________________________________________________________________
```
