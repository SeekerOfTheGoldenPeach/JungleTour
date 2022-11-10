import pickle
from Plant import *


def save_data(obj, filename):
    with open(filename, 'wb') as outp:
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)


def load_data(filename):
    with open(filename, 'rb') as f:
        x = pickle.load(f)
    return x
