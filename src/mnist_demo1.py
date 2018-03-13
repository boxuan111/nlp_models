# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Imports
import numpy as np
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)

config = tf.ConfigProto()
config.gpu_options.allow_growth =True
sess = tf.Session(config=config)
