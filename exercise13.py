import numpy as np
import math as log10

x = [1, 10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000]
x_log10 = [log10(k) for k x]
x_log10_array = np.log10(x)