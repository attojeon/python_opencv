'''
    - $ conda activate py36t21 (tensorflow2.1 가상환경 실행)
'''

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pillow 

np.set_printoptions(linewidth=150) # print의 출력폭을 충분히 확보
(t_images, t_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
train_images = t_images[:50000]
train_labels = t_labels[:50000]
eval_images = t_images[50000:]
eval_labels = t_labels[50000:]
print(train_images.shape, train_labels.shape, eval_images.shape, eval_labels.shape)
