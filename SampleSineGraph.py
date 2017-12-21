# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt 
import numpy as np 

def sinGraph():
    rate = 1000 
    frequency = 2 
    x = np.arange(rate)
    y = [math.sin(2*math.pi* frequency * (i/rate)) for i in x]
    plt.title("Sin Graph")
    plt.plot(x,y, 'b')
sinGraph()

