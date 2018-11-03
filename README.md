# cSociety
Code for a computer vision competition hosted by the Purdue IEEE Computer Society

This code has three major components: the actual training the neural network (keras_nn.py), evaluating the performance of the neural
network (keras_nn.py, test_nn.py, realtime_evaluate.py), and obtaining input data for the neural network (get_images.py, command line
tools).

The network has been able to attain an accuracy of 90% on testing data in its preliminary stages. However, not much has been done in order
to optimize this so far in the development of tools relating to the project, as establishing a data pipeline was the first priority.

Initial attempts to use ADADELTA as a training method have failed due to lack of convergence, so the network uses vanilla stochastic
gradient descent at the moment. However, the major alternative training methods are being explored and the final product will probably
use something more complicated.

The two primary libraries involved with this project are Keras/Tensorflow and OpenCV. OpenCV is used for the data pipeline and image
manipulation, and Keras is used to piece together and evaluate the network.

The test_results folder contains an example of what realtime_evaluate.py accomplishes, as well as an image of the current best testing
accuracy on an independent testing dataset.
