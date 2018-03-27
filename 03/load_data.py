import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
"""
Loading dataset:
1) Preload data into memory: write plain python code to load the data
    - Load data into an array, works if fits the RAM
    - No tensorflow specific 
    - Pandas: loading data and preprocessing for tensorflow
2) feed data step by step
    - Tensorflow calls your custom data loader function each time it needs more data
    - Possible to process large data set
    - Normal python code
3) custom data pipeline, best option for loading large dataset
    - Load data into memory with small chunks
    - Write tensorflow-specific code
    - Support parallel processing
"""
# Load training data set from CSV file
training_data_df =

# Pull out columns for X (data to train with) and Y (value to predict)
X_training =
Y_training =

# Load testing data set from CSV file
test_data_df =

# Pull out columns for X (data to train with) and Y (value to predict)
X_testing =
Y_testing =

# All data needs to be scaled to a small range like 0 to 1 for the neural
# network to work well. Create scalers for the inputs and outputs.
X_scaler =
Y_scaler =

# Scale both the training inputs and outputs
X_scaled_training =
Y_scaled_training =

# It's very important that the training and test data are scaled with the same scaler.
X_scaled_testing =
Y_scaled_testing =

print(X_scaled_testing.shape)
print(Y_scaled_testing.shape)

print("Note: Y values were scaled by multiplying by {:.10f} and adding {:.4f}".format(Y_scaler.scale_[0], Y_scaler.min_[0]))
