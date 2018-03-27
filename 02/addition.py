import os
import tensorflow as tf

# Turn off TensorFlow warning messages in program output
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Define computational graph
# placeholder node that gets assigned new values every time
# name is shown in the graphical representation of the model
X = tf.placeholder(tf.float32, name="X")
Y = tf.placeholder(tf.float32, name="Y")

# tells the tensorflow to link the value in the computation
addition = tf.add(X, Y, name="addition")

# pass in the operation we want to run
# Create the session
# ask session to run computation for our computation
with tf.Session() as session:
    # pass in the operation we want to run, also pass in the value for the placeholders
    # we pass in array, because tensorflow deals with tensor, which is
    # multidimensional array, because we are not adding together two numbers,
    # we are adding together two tensors
    result = session.run(addition, feed_dict={X: [1, 2, 10], Y: [4, 1, 10]})


    print(result)
