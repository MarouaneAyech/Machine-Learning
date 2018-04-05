# Linear regression is about approximating linear function on data
# given a data, we fit a model
# this model is limited by the family of linear functions of input features

# step 1: visualisation of data
# a synthetic dataset -> the function is 
# y = x/2 + sin(x) + N(0,1) [gaussian Noise]

# Visualisation is important : it gives an idea how complex the problem actually is
# and how to exactly solve the problem


# Step 2: Split the data into 3 sets
# - training (70%)
# - validation (15%)
# - test (15%)

# the protocol is to train the model on training set
# Then, after every episode training in order to evaluate HOW good the algorithm would generalize in the real world
# => we evaluate the model on the validation set
# Then after every episode-validation phase, we go bacj & tune the hyper parameters of the system:
# like change the kind of features
# like change model architecture
# number of nodes
# number of trees ...
# These are called Hyper parameters and they are not directly optimized by the Learning algorithm
# But they have to be observed based on the model performance on the validation-phase(HOW good the model generalizes to the real world)
# After the traing has been done, all the tuning of the architecture has been done, 
# we take the test set and we find the performance of the model on test set

# find performance of the model on the test set : it is reported as a measure of actual generalization
# because this test set was not shown to the model at any phase of its training - neither during its parameter learning 
# nor during its hyper parameters tuning

# Step 3: Fit  a linear model on the training set

