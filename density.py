import numpy as np
import matplotlib.pyplot as plt
def distance(x, o):
    return np.sqrt(4*np.cos(o)**2*(x**2-x)+1)

def sun(x):
    """
    Calculate density of the sun at a distance of x
    """

    return 6.5956*1e4*np.exp(-10.54*x)

def supernova(x):
    """
    Calculate density of a supernova at a distance of x
    """

    return 52.934/x**3
def earth(x):
    pass

def density(fm, fr, x, o):
    return fm(fr(x, o))

