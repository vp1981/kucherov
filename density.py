import numpy as np
import matplotlib.pyplot as plt
r = lambda x, o: np.sqrt(4*np.cos(o)**2*(x**2-x)+1)
def density(x):
    """
    Calculate density at a distance of x
    """

    return 6.5956*1e4*np.exp(-10.54*x)

