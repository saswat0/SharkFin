"""Tensorflow-Keras Implementation of SharkFin"""

## Import Necessary Modules
import tensorflow as tf
from tensorflow.keras.layers import Activation
from tensorflow.keras.utils import get_custom_objects

class SharkFin(Activation):
    '''
    SharkFin Activation Function.

    .. math::

        sharkfin(x) = tanh(e^{x}) * relu(-1, x) = tanh(e^{x}) * max(-1,x)

    Shape:
        - Input: Arbitrary. Use the keyword argument `input_shape`
        (tuple of integers, does not include the samples axis)
        when using this layer as the first layer in a model.

        - Output: Same shape as the input.

    Examples:
        >>> X = Activation('SharkFin', name="conv1_act")(X_input)
    '''

    def __init__(self, activation, **kwargs):
        super(SharkFin, self).__init__(activation, **kwargs)
        self.__name__ = 'SharkFin'


def sharkfin(inputs):
    return tf.math.tanh(tf.math.exp(inputs)) * tf.keras.activations.relu(inputs, threshold = -1.0)

get_custom_objects().update({'SharkFin': SharkFin(sharkfin)})
