import tensorflow as tf

# import mitdeeplearning as mdl

import numpy as np


a = tf.constant(10)
print(a)

# matrix = tf.constant([[1,2,3],[3,4,5]])
# row_vector = matrix[1]
# column_vector = matrix[:,2]
# scalar = matrix[1, 2]

# print("`row_vector`: {}".format(row_vector.numpy()))
# print("`column_vector`: {}".format(column_vector.numpy()))
# print("`scalar`: {}".format(scalar.numpy()))

# Create the nodes in the graph, and initialize values
a = tf.constant(15)
b = tf.constant(61)

# Add them!
c1 = tf.add(a,b)
c2 = a + b # TensorFlow overrides the "+" operation so that it is able to act on Tensors
print(c1)
print(c2)