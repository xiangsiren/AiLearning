#! /usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
# 安装 TensorFlow
import tensorflow as tf

from matplotlib import *
from matplotlib import pyplot as plt

x = np.arange(1, 11)
y = 2 * x + 5
print(x)
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x, y)
plt.show()