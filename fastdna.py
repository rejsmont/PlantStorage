import numpy as np
from datetime import datetime

def readfile(fname, chunk=None):
    """Read file and return a binary stream

    Keyword arguments:
    fname -- file name
    chunk -- buffer size (None for reading the whole file at once)
    """
    f = open(fname, 'rb')
    while True:
        buffer = f.read(chunk)
        if not buffer:
            break
        yield buffer
    f.close()
   
def encode(buffer):
    """Encode binary stream into base-4 numpy array

    Keyword arguments:
    buffer -- binary buffer
    """
    b = np.frombuffer(buffer, dtype='uint8')
    x = np.zeros(b.shape[0]*4, dtype='uint8')
    for i in range(4):
        x[i::4] = np.right_shift(b, i*2) & 3
    return x
  
def mutate(x, r):
    """Encode binary stream into base-4 numpy array

    Keyword arguments:
    x -- sequence in base-4 numpy array
    r -- mutation rate expressed as float (for example r=1/1000000)
    """
    rng = np.random.default_rng()
    m = rng.random(x.shape) < r
    v = np.zeros(x.shape, dtype='uint8')
    v[m] = rng.integers(3, size=v[m].shape, dtype='uint8') + 1
    return ((x + v) % 4)
  
def bases(a):
    """Convert base-4 sequence into ACTG sequence in numpy array

    Keyword arguments:
    a -- sequence in base-4 numpy array
    """
    s = np.zeros(x.shape, dtype=str)
    d = {0: 'A', 1: 'T', 2: 'C', 3: 'G'}
    for i in d.keys():
        s[x == i] = d[i] 
    return s
  
def decode(a):
    """Decode base-4 data into binary data

    Keyword arguments:
    a -- sequence in base-4 numpy array
    """
    x = np.zeros(round(a.shape[0]/4), dtype='uint8')
    for i in range(4):
        x = x | np.left_shift(a[i::4], i*2)
    return x
  
