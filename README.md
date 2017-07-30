# Bangla-Character-Recognition
Visual patterns recognition system which can recognise Hand-written Bangla characters using a Deep Convolutional Neural Network. This model achieved a top-1 prediction accuracy of 91.1 % which far surpassed the former recorded accuracy of 87.2 % in this project. This was developed in Theano, a python library specializes for Deep Learning Architectures.This project was a part of the Machine Learning course in the curriculum of the Computer Science department of IIT Roorkee.

Dataset:
The dataset was obtained online from the CMATERdb pattern recognition database repository. It consists of a 12,000 Training images and 3,000 Testing images in the dataset comprised by 222 characters of Bangla language. 


Architecture of the network:
- Images normalized to the size of 32x32 for input to the model. 
- Model contains 2 sequential steps each comprising two convolutional layers(each with a relu activation), a maxpooling layer   and finally a dropout to avoid overfitting.

- Above model is followed by two densely connected layers of neural network. Activation layer used is Softmax. 

Results:
Top-1 accuracy obtained on the testing data by this model: 91.7%

